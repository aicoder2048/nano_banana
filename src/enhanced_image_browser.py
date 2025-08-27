"""增强版图片浏览器 - 多列布局、目录导航和更好的用户体验"""

import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt

@dataclass
class ImageInfo:
    """图片信息"""
    path: str
    name: str
    size: int
    directory: str
    relative_path: str

@dataclass
class DirectoryInfo:
    """目录信息"""
    path: str
    name: str
    image_count: int
    subdirs: List['DirectoryInfo']

class EnhancedImageBrowser:
    """增强版图片浏览器"""
    
    SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.heic', '.webp'}
    
    def __init__(self, console: Console):
        self.console = console
        self.current_directory = Path.cwd()
        self.keyboard_mode = False
        
    def _format_file_size(self, size: int) -> str:
        """格式化文件大小"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}TB"
    
    
    def _scan_images_in_directory(self, directory: Path, recursive: bool = True) -> Tuple[List[ImageInfo], List[DirectoryInfo]]:
        """扫描目录中的图片和子目录"""
        images = []
        subdirs = []
        
        if not directory.exists() or not directory.is_dir():
            return images, subdirs
        
        try:
            items = list(directory.iterdir())
            items.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
            
            for item in items:
                if item.name.startswith('.'):
                    continue
                    
                if item.is_file() and item.suffix.lower() in self.SUPPORTED_FORMATS:
                    try:
                        size = item.stat().st_size
                        images.append(ImageInfo(
                            path=str(item),
                            name=item.name,
                            size=size,
                            directory=str(directory),
                            relative_path=str(item.relative_to(self.current_directory))
                        ))
                    except (OSError, ValueError):
                        continue
                        
                elif item.is_dir() and recursive:
                    try:
                        # 递归统计子目录的图片
                        subdir_images, sub_subdirs = self._scan_images_in_directory(item, recursive=True)
                        
                        if subdir_images or sub_subdirs:
                            subdirs.append(DirectoryInfo(
                                path=str(item),
                                name=item.name,
                                image_count=len(subdir_images) + sum(s.image_count for s in sub_subdirs),
                                subdirs=sub_subdirs
                            ))
                            # 将子目录的图片也加入到结果中
                            images.extend(subdir_images)
                            
                    except (OSError, PermissionError):
                        continue
                        
        except (OSError, PermissionError):
            pass
            
        return images, subdirs
    
    def _show_directory_tree(self, subdirs: List[DirectoryInfo], current_level: int = 0) -> None:
        """显示目录树结构"""
        if not subdirs:
            return
            
        for i, subdir in enumerate(subdirs):
            indent = "  " * current_level
            is_last = i == len(subdirs) - 1
            connector = "└── " if is_last else "├── "
            
            self.console.print(f"{indent}{connector}📁 [bold cyan]{subdir.name}[/bold cyan] [dim]({subdir.image_count} images)[/dim]")
            
            # 递归显示子目录（限制层级避免过深）
            if current_level < 3 and subdir.subdirs:
                self._show_directory_tree(subdir.subdirs, current_level + 1)
    
    def _create_multi_column_list(self, images: List[ImageInfo], selected_indices: set = None, start_idx: int = 0):
        """多列简洁图片列表显示"""
        if selected_indices is None:
            selected_indices = set()
        
        # 每页显示数量和列数
        display_count = min(24, len(images))  # 增加到24个，适合多列
        terminal_width = self.console.size.width
        
        # 计算列数 - 每列至少25个字符
        cols = min(4, max(2, terminal_width // 25))
        rows = (display_count + cols - 1) // cols
        
        # 创建网格数据
        for row in range(rows):
            row_items = []
            
            for col in range(cols):
                idx = row + col * rows
                if idx < display_count and idx < len(images):
                    img = images[idx]
                    global_idx = start_idx + idx
                    is_selected = global_idx in selected_indices
                    
                    # 简化文件名
                    name = img.name
                    max_name_len = 20  # 每列最多20字符
                    if len(name) > max_name_len:
                        name = name[:max_name_len-3] + "..."
                    
                    # 格式化显示
                    if is_selected:
                        item = f"[green]✓{idx + 1:2d}. {name:<{max_name_len}}[/green]"
                    else:
                        item = f" {idx + 1:2d}. {name:<{max_name_len}}"
                    
                    row_items.append(item)
                else:
                    row_items.append(" " * 25)  # 空白填充
            
            # 输出一行
            self.console.print("  ".join(row_items))
        
        # 翻页提示
        if len(images) > display_count:
            self.console.print(f"\\n[dim]... +{len(images) - display_count} more (n for next)[/dim]")
    
    def _paginated_selection(self, images: List[ImageInfo], page_size: int = None) -> Optional[List[str]]:
        """分页选择图片 - 智能优化大量图片处理"""
        if not images:
            self.console.print("[yellow]未找到任何图片[/yellow]")
            return None
        
        # 智能调整页面大小
        if page_size is None:
            terminal_height = self.console.size.height
            if len(images) > 1000:
                page_size = 50  # 大量图片时增加每页显示数量
            elif len(images) > 100:
                page_size = 30
            else:
                page_size = 20
        
        total_pages = (len(images) + page_size - 1) // page_size
        current_page = 0
        selected_indices = set()
        
        # 性能优化：对于大量图片，显示警告并提供批量操作
        if len(images) > 500:
            self.console.print(f"[yellow]⚠️  检测到大量图片 ({len(images)} 张)，建议使用批量操作提高效率[/yellow]")
        
        while True:
            start_idx = current_page * page_size
            end_idx = min(start_idx + page_size, len(images))
            page_images = images[start_idx:end_idx]
            
            self.console.clear()
            
            # 简化页眉
            self.console.print(f"\\n[bold cyan]Select Images - Page {current_page + 1}/{total_pages}[/bold cyan]")
            self.console.print()
            
            # 多列简洁图片列表
            self._create_multi_column_list(page_images, selected_indices, start_idx)
            
            # 极简状态显示
            if selected_indices:
                self.console.print(f"\\n[green]Selected: {len(selected_indices)} images[/green]")
            
            # 极简操作提示
            options = []
            if current_page > 0:
                options.append("p=prev")
            if current_page < total_pages - 1:
                options.append("n=next")
            options.append("done=finish")
            
            if options:
                self.console.print(f"[dim]{' | '.join(options)}[/dim]")
            
            # 使用可靠的文本输入
            choice = self.console.input("\\nEnter numbers (e.g. 1,3,5) or p/n for pages: ").strip().lower()
            
            # 处理用户输入
            result = self._handle_selection_input(
                choice, images, page_images, selected_indices, 
                current_page, total_pages, start_idx, end_idx
            )
            
            if result == "exit":
                return None
            elif result == "done":
                if selected_indices:
                    return [images[i].path for i in sorted(selected_indices)]
                else:
                    self.console.print("[yellow]未选择任何图片，请至少选择一张图片[/yellow]")
                    self.console.input("按 Enter 继续...")
                    continue
            elif result == "clear":
                selected_indices.clear()
            elif isinstance(result, int):
                current_page = result
    
    def _calculate_optimal_columns(self, image_count: int) -> int:
        """根据图片数量和终端宽度计算最佳列数 - 避免混淆"""
        terminal_width = self.console.size.width
        
        # 为了避免混淆，最多使用2列，让用户清楚这是统一的选择列表
        if image_count <= 10:
            return 1  # 少量图片使用单列，最清晰
        elif terminal_width >= 120:
            return 2  # 宽屏幕使用双列
        else:
            return 1  # 窄屏幕保持单列
    
    
    def _handle_selection_input(self, choice: str, all_images: List[ImageInfo], page_images: List[ImageInfo], 
                               selected_indices: set, current_page: int, total_pages: int, 
                               start_idx: int, end_idx: int) -> str:
        """处理选择输入并返回操作结果 - 简化版本"""
        
        choice = choice.strip()
        
        # 退出和完成
        if choice.lower() in ['q', 'quit', 'cancel']:
            return "exit"
        elif choice.lower() in ['done', 'd', ''] or choice == '\\n':  # Enter键也算完成
            return "done"
        
        # 导航
        elif choice.lower() in ['p', 'prev'] and current_page > 0:
            return current_page - 1
        elif choice.lower() in ['n', 'next'] and current_page < total_pages - 1:
            return current_page + 1
        
        # 批量选择
        elif choice.lower() in ['all', 'page-all']:
            for i in range(start_idx, end_idx):
                selected_indices.add(i)
            self.console.print(f"[green]✓ 已选择当前页所有 {len(page_images)} 张图片[/green]")
            import time
            time.sleep(0.8)
            return current_page
            
        else:
            # 解析多选输入 (如: "1,3,5" 或 "1-3" 或 "1")
            return self._parse_multi_selection(choice, all_images, selected_indices, start_idx, end_idx, current_page)
    
    def _parse_multi_selection(self, input_str: str, all_images: List[ImageInfo], 
                              selected_indices: set, start_idx: int, end_idx: int, current_page: int) -> int:
        """解析多选输入，支持 1,3,5 和 1-3 格式"""
        try:
            # 清理输入
            input_str = input_str.replace(' ', '')
            selected_numbers = []
            
            # 解析逗号分隔的输入
            parts = input_str.split(',')
            
            for part in parts:
                if '-' in part:
                    # 处理范围 (如 1-3)
                    try:
                        start, end = map(int, part.split('-'))
                        if start > end:
                            start, end = end, start
                        selected_numbers.extend(range(start, end + 1))
                    except ValueError:
                        self.console.print(f"[red]⚠️  无效范围格式: '{part}'[/red]")
                        self.console.input("按 Enter 继续...")
                        return current_page
                else:
                    # 处理单个数字
                    try:
                        num = int(part)
                        selected_numbers.append(num)
                    except ValueError:
                        self.console.print(f"[red]⚠️  无效数字: '{part}'[/red]")
                        self.console.input("按 Enter 继续...")
                        return current_page
            
            # 验证并应用选择
            valid_selections = []
            invalid_selections = []
            
            for num in selected_numbers:
                if 1 <= num <= (end_idx - start_idx):
                    global_idx = start_idx + num - 1
                    valid_selections.append((num, global_idx, all_images[global_idx].name))
                else:
                    invalid_selections.append(num)
            
            # 显示无效选择
            if invalid_selections:
                max_num = end_idx - start_idx
                self.console.print(f"[red]⚠️  无效编号: {invalid_selections} (请输入 1-{max_num})[/red]")
            
            # 应用有效选择 - 简化反馈
            if valid_selections:
                added = 0
                removed = 0
                for num, global_idx, name in valid_selections:
                    if global_idx in selected_indices:
                        selected_indices.remove(global_idx)
                        removed += 1
                    else:
                        selected_indices.add(global_idx)
                        added += 1
                
                # 简化状态反馈
                if added > 0:
                    self.console.print(f"[green]+ {added} selected[/green]")
                if removed > 0:
                    self.console.print(f"[yellow]- {removed} removed[/yellow]")
                
                import time
                time.sleep(0.8)
            
            return current_page
            
        except Exception as e:
            self.console.print(f"[red]⚠️  输入解析错误: {e}[/red]")
            self.console.print("[dim]提示: 请输入如 '1', '1,3,5' 或 '1-3' 格式[/dim]")
            self.console.input("按 Enter 继续...")
            return current_page
    
    def _smart_selection(self, images: List[ImageInfo], selected_indices: set) -> int:
        """智能选择图片"""
        self.console.print("\\n[bold]智能选择选项:[/bold]")
        self.console.print("[green]1.[/green] 选择最大的图片 (前10张)")
        self.console.print("[green]2.[/green] 选择最小的图片 (前10张)")
        self.console.print("[green]3.[/green] 选择特定格式 (jpg, png, etc.)")
        self.console.print("[green]4.[/green] 按文件名包含关键词选择")
        
        smart_choice = Prompt.ask("智能选择方式", choices=["1", "2", "3", "4"], default="1")
        
        if smart_choice == "1":
            # 按大小排序，选择最大的
            sorted_images = sorted(enumerate(images), key=lambda x: x[1].size, reverse=True)
            for i, (original_idx, img) in enumerate(sorted_images[:10]):
                selected_indices.add(original_idx)
            self.console.print("[green]已选择前10张最大的图片[/green]")
            
        elif smart_choice == "2":
            # 选择最小的
            sorted_images = sorted(enumerate(images), key=lambda x: x[1].size)
            for i, (original_idx, img) in enumerate(sorted_images[:10]):
                selected_indices.add(original_idx)
            self.console.print("[green]已选择前10张最小的图片[/green]")
            
        elif smart_choice == "3":
            # 按格式选择
            formats = set()
            for img in images:
                ext = os.path.splitext(img.name)[1].lower()
                if ext:
                    formats.add(ext)
            
            self.console.print(f"可用格式: {', '.join(sorted(formats))}")
            target_format = self.console.input("输入要选择的格式 (如: .jpg): ").strip().lower()
            
            if not target_format.startswith('.'):
                target_format = '.' + target_format
            
            count = 0
            for i, img in enumerate(images):
                if os.path.splitext(img.name)[1].lower() == target_format:
                    selected_indices.add(i)
                    count += 1
            
            self.console.print(f"[green]已选择 {count} 张 {target_format} 格式的图片[/green]")
            
        elif smart_choice == "4":
            # 按关键词选择
            keyword = self.console.input("输入文件名关键词: ").strip().lower()
            if keyword:
                count = 0
                for i, img in enumerate(images):
                    if keyword in img.name.lower():
                        selected_indices.add(i)
                        count += 1
                self.console.print(f"[green]已选择 {count} 张包含 '{keyword}' 的图片[/green]")
        
        self.console.input("按 Enter 继续...")
        return 0  # 返回第一页
    
    def _filter_selection(self, images: List[ImageInfo], selected_indices: set) -> int:
        """按模式筛选图片"""
        pattern = self.console.input("输入文件名模式 (如: IMG_*, *.jpg, *2024*): ").strip()
        
        if pattern:
            import fnmatch
            count = 0
            for i, img in enumerate(images):
                if fnmatch.fnmatch(img.name.lower(), pattern.lower()):
                    selected_indices.add(i)
                    count += 1
            self.console.print(f"[green]已选择 {count} 张匹配模式 '{pattern}' 的图片[/green]")
        
        self.console.input("按 Enter 继续...")
        return 0
    
    def _handle_range_selection(self, images: List[ImageInfo], selected_indices: set, start_idx: int, end_idx: int) -> int:
        """处理范围选择"""
        range_input = self.console.input("输入范围 (如: 1-5 或 1,3,5): ").strip()
        try:
            indices = self._parse_range_input(range_input, start_idx + 1, end_idx)
            for idx in indices:
                global_idx = start_idx + idx - (start_idx + 1)
                if global_idx in selected_indices:
                    selected_indices.remove(global_idx)
                else:
                    selected_indices.add(global_idx)
        except ValueError as e:
            self.console.print(f"[red]范围输入错误: {e}[/red]")
            self.console.input("按 Enter 继续...")
        
        return -1  # 保持当前页
    
    def _parse_range_input(self, range_str: str, start: int, end: int) -> List[int]:
        """解析范围输入"""
        indices = []
        parts = range_str.replace(' ', '').split(',')
        
        for part in parts:
            if '-' in part:
                # 范围输入 (如 1-5)
                try:
                    range_start, range_end = map(int, part.split('-'))
                    if range_start > range_end:
                        range_start, range_end = range_end, range_start
                    
                    for i in range(max(start, range_start), min(end + 1, range_end + 1)):
                        if i not in indices:
                            indices.append(i)
                except ValueError:
                    raise ValueError(f"无效范围格式: {part}")
            else:
                # 单个数字
                try:
                    num = int(part)
                    if start <= num <= end and num not in indices:
                        indices.append(num)
                except ValueError:
                    raise ValueError(f"无效数字: {part}")
        
        return indices
    
    def browse_and_select_images(self, directory: str = None, max_images: int = 10) -> List[str]:
        """浏览并选择图片"""
        if directory:
            self.current_directory = Path(directory)
        
        while True:
            self.console.clear()
            self.console.print(f"\\n[bold cyan]🔍 当前目录: {self.current_directory}[/bold cyan]")
            
            # 扫描图片
            with self.console.status("扫描图片中..."):
                images, subdirs = self._scan_images_in_directory(self.current_directory, recursive=True)
            
            # 显示目录导航选项
            self._show_directory_navigation_options()
            
            if not images:
                self.console.print("[red]在当前目录及子目录中未找到任何图片文件[/red]")
                
                nav_choice = Prompt.ask(
                    "选择操作",
                    choices=["parent", "change", "exit"],
                    default="parent"
                )
                
                if nav_choice == "parent":
                    parent = self.current_directory.parent
                    if parent != self.current_directory:  # 不是根目录
                        self.current_directory = parent
                        continue
                    else:
                        self.console.print("[yellow]已经在根目录[/yellow]")
                        self.console.input("按 Enter 继续...")
                        continue
                elif nav_choice == "change":
                    if self._change_directory():
                        continue
                    else:
                        continue
                else:
                    return []
            
            # 显示目录结构概览
            if subdirs:
                self.console.print(f"\\n[bold]📁 目录结构:[/bold]")
                self._show_directory_tree(subdirs)
            
            self.console.print(f"\\n[bold green]✅ 找到 {len(images)} 张图片[/bold green]")
            
            # 极简选择界面
            self.console.print("\\n[bold]Options:[/bold]")
            self.console.print("1. Select images")
            
            choices = ["1", "q"]
            if self.current_directory.parent != self.current_directory:
                self.console.print("2. Go up")
                choices.insert(-1, "2")
            self.console.print("q. Quit")
            
            try:
                method = Prompt.ask("Choose", choices=choices, default="1")
            except (KeyboardInterrupt, EOFError):
                method = "q"
            
            if method == "1":
                # 开始交互式选择
                result = self._paginated_selection(images)
                if result is not None:
                    return result
            elif method == "2":
                # 返回上级目录
                parent = self.current_directory.parent
                if parent != self.current_directory:
                    self.current_directory = parent
                    continue
                else:
                    self.console.print("[yellow]已经在根目录[/yellow]")
                    self.console.input("按 Enter 继续...")
                    continue
            elif method.lower() == "q":
                # 退出选择
                return []
        
        return []
    
    def _show_directory_navigation_options(self):
        """显示目录导航选项"""
        parent = self.current_directory.parent
        
        nav_info = []
        if parent != self.current_directory:
            nav_info.append(f"⬆️  上级: [blue]{parent.name}[/blue]")
        
        # 显示当前目录的子目录（只显示包含图片的）
        try:
            subdirs_with_images = []
            for item in self.current_directory.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    images, _ = self._scan_images_in_directory(item, recursive=True)
                    if images:
                        subdirs_with_images.append((item.name, len(images)))
            
            if subdirs_with_images:
                nav_info.append("📁 子目录: " + " | ".join([f"[cyan]{name}[/cyan] ({count})" for name, count in subdirs_with_images[:5]]))
                if len(subdirs_with_images) > 5:
                    nav_info.append(f"[dim]... 以及其他 {len(subdirs_with_images) - 5} 个目录[/dim]")
        
        except (OSError, PermissionError):
            nav_info.append("[red]无法读取目录信息[/red]")
        
        if nav_info:
            self.console.print("[dim]" + " | ".join(nav_info) + "[/dim]\\n")
    
    def _change_directory(self) -> bool:
        """切换到新目录"""
        self.console.print("\\n[bold]目录导航:[/bold]")
        self.console.print("[green]1.[/green] 输入完整路径")
        self.console.print("[green]2.[/green] 选择当前目录的子目录")
        self.console.print("[green]3.[/green] 使用相对路径")
        
        nav_method = Prompt.ask("导航方式", choices=["1", "2", "3"], default="2")
        
        try:
            if nav_method == "1":
                # 完整路径输入
                new_path = self.console.input("请输入目录路径: ").strip()
                if not new_path:
                    return False
                
                expanded_path = Path(os.path.expanduser(new_path))
                if expanded_path.exists() and expanded_path.is_dir():
                    self.current_directory = expanded_path
                    return True
                else:
                    self.console.print(f"[red]目录不存在: {new_path}[/red]")
                    self.console.input("按 Enter 继续...")
                    return False
                    
            elif nav_method == "2":
                # 选择子目录
                subdirs = []
                try:
                    for item in self.current_directory.iterdir():
                        if item.is_dir() and not item.name.startswith('.'):
                            subdirs.append(item)
                    
                    if not subdirs:
                        self.console.print("[yellow]当前目录没有子目录[/yellow]")
                        self.console.input("按 Enter 继续...")
                        return False
                    
                    # 显示子目录列表
                    self.console.print("\\n[bold]可用子目录:[/bold]")
                    for i, subdir in enumerate(subdirs, 1):
                        self.console.print(f"[green]{i}.[/green] {subdir.name}")
                    
                    choice = IntPrompt.ask(f"选择目录 (1-{len(subdirs)})", default=1)
                    if 1 <= choice <= len(subdirs):
                        self.current_directory = subdirs[choice - 1]
                        return True
                    else:
                        return False
                        
                except (OSError, PermissionError):
                    self.console.print("[red]无法读取目录[/red]")
                    self.console.input("按 Enter 继续...")
                    return False
                    
            elif nav_method == "3":
                # 相对路径
                rel_path = self.console.input("相对路径 (如: ../images, ./photos): ").strip()
                if not rel_path:
                    return False
                
                new_path = self.current_directory / rel_path
                resolved_path = new_path.resolve()
                
                if resolved_path.exists() and resolved_path.is_dir():
                    self.current_directory = resolved_path
                    return True
                else:
                    self.console.print(f"[red]目录不存在: {rel_path}[/red]")
                    self.console.input("按 Enter 继续...")
                    return False
                    
        except Exception as e:
            self.console.print(f"[red]目录切换错误: {e}[/red]")
            self.console.input("按 Enter 继续...")
            return False
        
        return False
    
    def _browse_by_directory(self, subdirs: List[DirectoryInfo], all_images: List[ImageInfo]) -> Optional[List[str]]:
        """按目录浏览选择图片"""
        # 按目录分组图片
        dir_images = {}
        for img in all_images:
            if img.directory not in dir_images:
                dir_images[img.directory] = []
            dir_images[img.directory].append(img)
        
        selected_paths = []
        
        # 显示目录选择
        directories = list(dir_images.keys())
        directories.sort()
        
        while True:
            self.console.clear()
            self.console.print("\\n[bold cyan]📁 按目录选择图片[/bold cyan]\\n")
            
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("编号", style="bold green", width=6)
            table.add_column("目录", style="white")
            table.add_column("图片数", style="yellow", width=10)
            
            for i, dir_path in enumerate(directories, 1):
                rel_dir = str(Path(dir_path).relative_to(self.current_directory))
                if rel_dir == ".":
                    rel_dir = "[当前目录]"
                
                table.add_row(
                    str(i),
                    rel_dir,
                    str(len(dir_images[dir_path]))
                )
            
            self.console.print(table)
            
            if selected_paths:
                self.console.print(f"\\n[yellow]已选择 {len(selected_paths)} 张图片[/yellow]")
            
            self.console.print("\\n[bold]操作:[/bold]")
            self.console.print(f"[green]1-{len(directories)}[/green]: 选择目录浏览")
            self.console.print("[cyan]done[/cyan]: 完成选择")
            self.console.print("[red]cancel[/red]: 取消")
            
            choice = self.console.input("\\n请选择: ").strip().lower()
            
            if choice == 'cancel':
                return None
            elif choice == 'done':
                return selected_paths
            else:
                try:
                    dir_idx = int(choice) - 1
                    if 0 <= dir_idx < len(directories):
                        selected_dir = directories[dir_idx]
                        dir_selected = self._paginated_selection(dir_images[selected_dir])
                        if dir_selected:
                            selected_paths.extend(dir_selected)
                    else:
                        self.console.print("[red]无效选择[/red]")
                        self.console.input("按 Enter 继续...")
                except ValueError:
                    self.console.print("[red]无效输入[/red]")
                    self.console.input("按 Enter 继续...")
        
        return selected_paths

# 工厂函数
def create_enhanced_browser(console: Console) -> EnhancedImageBrowser:
    """创建增强版图片浏览器实例"""
    return EnhancedImageBrowser(console)