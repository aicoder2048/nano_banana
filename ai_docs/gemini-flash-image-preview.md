::::::::::::::::::::::::::::::::: {#main-content .devsite-main-content role="main" has-book-nav="" has-sidebar=""}
:::: devsite-sidebar
::: devsite-sidebar-content
:::
::::

::::: {.devsite-banner .devsite-banner-announcement .nocontent background="google-blue"}
:::: devsite-banner-message
::: devsite-banner-message-text
Gemini 2.5 Flash Image Preview is now available in the Gemini API!
[Learn
more](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/){.button
.button-primary}
:::
::::
:::::

::: {.devsite-article-meta .nocontent role="navigation"}
- [Home](https://ai.google.dev/){.devsite-breadcrumb-link
  .gc-analytics-event category="Site-Wide Custom Events"
  data-label="Breadcrumbs" data-value="1" track-type="globalNav"
  track-name="breadcrumb" track-metadata-position="1"
  track-metadata-eventdetail=""}

- ::: {.devsite-breadcrumb-guillemet .material-icons aria-hidden="true"}
  :::

  [Gemini
  API](https://ai.google.dev/gemini-api){.devsite-breadcrumb-link
  .gc-analytics-event category="Site-Wide Custom Events"
  data-label="Breadcrumbs" data-value="2" track-type="globalNav"
  track-name="breadcrumb" track-metadata-position="2"
  track-metadata-eventdetail="Gemini API"}

- ::: {.devsite-breadcrumb-guillemet .material-icons aria-hidden="true"}
  :::

  [Gemini API
  docs](https://ai.google.dev/gemini-api/docs){.devsite-breadcrumb-link
  .gc-analytics-event category="Site-Wide Custom Events"
  data-label="Breadcrumbs" data-value="3" track-type="globalNav"
  track-name="breadcrumb" track-metadata-position="3"
  track-metadata-eventdetail=""}
:::

Send feedback

# Gemini models {#gemini-models .devsite-page-title tabindex="-1"}

::: {.devsite-actions hidden="" nosnippet=""}
:::

::: devsite-page-title-meta
:::

:::::::::::::::::::::: {.devsite-article-body .clearfix}
:::::: gemini-api-recommended
::: gemini-api-card
2.5 Pro [spark]{.google-symbols aria-hidden="true" translate="no"}

Our most powerful thinking model with maximum response accuracy and
state-of-the-art performance

- Input audio, images, video, and text, get text responses
- Tackle difficult problems, analyze large databases, and more
- Best for complex coding, reasoning, and multimodal understanding

[](#gemini-2.5-pro){aria-label="Learn more about 2.5 Pro"}
:::

::: gemini-api-card
2.5 Flash [spark]{.google-symbols aria-hidden="true" translate="no"}

Our best model in terms of price-performance, offering well-rounded
capabilities.

- Input audio, images, video, and text, and get text responses
- Model thinks as needed; or, you can configure a thinking budget
- Best for low latency, high volume tasks that require thinking

[](#gemini-2.5-flash){aria-label="Learn more about 2.5 Flash"}
:::

::: gemini-api-card
2.5 Flash-Lite [spark]{.google-symbols aria-hidden="true"
translate="no"}

A Gemini 2.5 Flash model optimized for cost efficiency and low latency.

- Input audio, images, video, and text, and get text responses
- Most cost-efficient model supporting high throughput
- Best for real time, low latency use cases

[](#gemini-2.5-flash-lite){aria-label="Learn more about 2.5 Flash-Lite"}
:::
::::::

**Note:** Gemini 2.5 Pro and 2.5 Flash come with ***thinking on by
default***. If you\'re migrating from a non-thinking model such as 2.0
Pro or Flash, we recommend you to review the [Thinking
guide](/gemini-api/docs/thinking) first.

## Model variants {#model-variations data-text="Model variants" tabindex="-1"}

The Gemini API offers different models that are optimized for specific
use cases. Here\'s a brief overview of Gemini variants that are
available:

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Model variant                                                        Input(s)          Output            Optimized for
  -------------------------------------------------------------------- ----------------- ----------------- -----------------------------------------
  [Gemini 2.5 Pro](#gemini-2.5-pro)\                                   Audio, images,    Text              Enhanced thinking and reasoning,
  `gemini-2.5-pro`{translate="no" dir="ltr"}                           videos, text, and                   multimodal understanding, advanced
                                                                       PDF                                 coding, and more

  [Gemini 2.5 Flash](#gemini-2.5-flash)\                               Audio, images,    Text              Adaptive thinking, cost efficiency
  `gemini-2.5-flash`{translate="no" dir="ltr"}                         videos, and text                    

  [Gemini 2.5 Flash-Lite](#gemini-2.5-flash-lite)\                     Text, image,      Text              Most cost-efficient model supporting high
  `gemini-2.5-flash-lite`{translate="no" dir="ltr"}                    video, audio                        throughput

  [Gemini 2.5 Flash Live](#live-api)\                                  Audio, video, and Text, audio       Low-latency bidirectional voice and video
  `gemini-live-2.5-flash-preview`{translate="no" dir="ltr"}            text                                interactions

  [Gemini 2.5 Flash Native Audio](#gemini-2.5-flash-native-audio)\     Audio, videos,    Text and audio,   High quality, natural conversational
  `gemini-2.5-flash-preview-native-audio-dialog`{translate="no"        and text          interleaved       audio outputs, with or without thinking
  dir="ltr"} &\                                                                                            
  `gemini-2.5-flash-exp-native-audio-thinking-dialog`{translate="no"                                       
  dir="ltr"}                                                                                               

  [Gemini 2.5 Flash Image Preview](#gemini-2.5-flash-image-preview)\   Images and text   Images and text   Precise, conversational image generation
  `gemini-2.5-flash-image-preview`{translate="no" dir="ltr"}                                               and editing

  [Gemini 2.5 Flash Preview TTS](#gemini-2.5-flash-preview-tts)\       Text              Audio             Low latency, controllable, single- and
  `gemini-2.5-flash-preview-tts`{translate="no" dir="ltr"}                                                 multi-speaker text-to-speech audio
                                                                                                           generation

  [Gemini 2.5 Pro Preview TTS](#gemini-2.5-pro-preview-tts)\           Text              Audio             Low latency, controllable, single- and
  `gemini-2.5-pro-preview-tts`{translate="no" dir="ltr"}                                                   multi-speaker text-to-speech audio
                                                                                                           generation

  [Gemini 2.0 Flash](#gemini-2.0-flash)\                               Audio, images,    Text              Next generation features, speed, and
  `gemini-2.0-flash`{translate="no" dir="ltr"}                         videos, and text                    realtime streaming.

  [Gemini 2.0 Flash Preview Image                                      Audio, images,    Text, images      Conversational image generation and
  Generation](#gemini-2.0-flash-preview-image-generation)\             videos, and text                    editing
  `gemini-2.0-flash-preview-image-generation`{translate="no"                                               
  dir="ltr"}                                                                                               

  [Gemini 2.0 Flash-Lite](#gemini-2.0-flash-lite)\                     Audio, images,    Text              Cost efficiency and low latency
  `gemini-2.0-flash-lite`{translate="no" dir="ltr"}                    videos, and text                    

  [Gemini 2.0 Flash Live](#live-api-2.0)\                              Audio, video, and Text, audio       Low-latency bidirectional voice and video
  `gemini-2.0-flash-live-001`{translate="no" dir="ltr"}                text                                interactions

  [Gemini 1.5 Flash](#gemini-1.5-flash)\                               Audio, images,    Text              Fast and versatile performance across a
  `gemini-1.5-flash`{translate="no" dir="ltr"}                         videos, and text                    diverse variety of tasks\
                                                                                                           [Deprecated]{.gemini-api-not-supported}

  [Gemini 1.5 Flash-8B](#gemini-1.5-flash-8b)\                         Audio, images,    Text              High volume and lower intelligence tasks\
  `gemini-1.5-flash-8b`{translate="no" dir="ltr"}                      videos, and text                    [Deprecated]{.gemini-api-not-supported}

  [Gemini 1.5 Pro](#gemini-1.5-pro)\                                   Audio, images,    Text              Complex reasoning tasks requiring more
  `gemini-1.5-pro`{translate="no" dir="ltr"}                           videos, and text                    intelligence\
                                                                                                           [Deprecated]{.gemini-api-not-supported}
  --------------------------------------------------------------------------------------------------------------------------------------------------

You can view the rate limits for each model on the [rate limits
page](/gemini-api/docs/rate-limits).

::: section
### Gemini 2.5 Pro {#gemini-2.5-pro .showalways data-text="Gemini 2.5 Pro" tabindex="-1"}

Gemini 2.5 Pro is our state-of-the-art thinking model, capable of
reasoning over complex problems in code, math, and STEM, as well as
analyzing large datasets, codebases, and documents using long context.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.5-pro){.gemini-api-model-button}

#### Model details {#model-details data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `gemini-2.5-pro`{translate="no" dir="ltr"}               |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, images, video, text, and PDF                      |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 65,536                                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search grounding**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Batch Mode**                                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **URL Context**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - `Stable: gemini-2.5-pro`{translate="no" dir="ltr"}     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | June 2025                                                |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | January 2025                                             |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.5 Flash {#gemini-2.5-flash .showalways data-text="Gemini 2.5 Flash" tabindex="-1"}

Our best model in terms of price-performance, offering well-rounded
capabilities. 2.5 Flash is best for large scale processing, low-latency,
high volume tasks that require thinking, and agentic use cases.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.5-flash){.gemini-api-model-button}

#### Model details {#model-details_1 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.5-flash`{translate="no" dir="ltr"}      |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Text, images, video, audio                               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 65,536                                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search grounding**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Batch Mode**                                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **URL Context**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Stable: `gemini-2.5-flash`{translate="no" dir="ltr"}   |
|                                               | - Preview:                                               |
|                                               |   `gemini-2.5-flash-preview-05-20`{translate="no"        |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | June 2025                                                |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | January 2025                                             |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.5 Flash-Lite {#gemini-2.5-flash-lite .showalways data-text="Gemini 2.5 Flash-Lite" tabindex="-1"}

A Gemini 2.5 Flash model optimized for cost-efficiency and high
throughput.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.5-flash-lite){.gemini-api-model-button}

#### Model details {#model-details_2 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.5-flash-lite`{translate="no" dir="ltr"} |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Text, image, video, audio, PDF                           |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 65,536                                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **URL Context**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search grounding**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Batch mode**                                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **URL Context**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Stable: `gemini-2.5-flash-lite`{translate="no"         |
|                                               |   dir="ltr"}                                             |
|                                               | - Preview: `gemini-2.5-flash-lite-06-17`{translate="no"  |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | July 2025                                                |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | January 2025                                             |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.5 Flash Live {#live-api .showalways data-text="Gemini 2.5 Flash Live" tabindex="-1"}

The Gemini 2.5 Flash Live model works with the Live API to enable
low-latency bidirectional voice and video interactions with Gemini. The
model can process text, audio, and video input, and it can provide text
and audio output.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-live-2.5-flash-preview){.gemini-api-model-button}

#### Model details {#model-details_3 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-live-2.5-flash-preview`{translate="no"    |
| aria-hidden="true"}Model code                 | dir="ltr"}                                               |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, video, and text                                   |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text, and audio                                          |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **URL context**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Preview:                                               |
|                                               |   `gemini-live-2.5-flash-preview`{translate="no"         |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | June 2025                                                |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | January 2025                                             |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.5 Flash Native Audio {#gemini-2.5-flash-native-audio .showalways data-text="Gemini 2.5 Flash Native Audio" tabindex="-1"}

Our native audio dialog models, with and without thinking, available
through the [Live API](/gemini-api/docs/live). These models provide
interactive and unstructured conversational experiences, with style and
control prompting.

[Try native audio in Google AI
Studio](https://aistudio.google.com/app/live){.gemini-api-model-button}

#### Model details {#model-details_4 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+---------------------------------------------------------------------------+
| Property                                      | Description                                                               |
+===============================================+===========================================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.5-flash-preview-native-audio-dialog`{translate="no"      |
| aria-hidden="true"}Model code                 | dir="ltr"} &\                                                             |
|                                               | `models/gemini-2.5-flash-exp-native-audio-thinking-dialog`{translate="no" |
|                                               | dir="ltr"}                                                                |
+-----------------------------------------------+---------------------------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                                               |
| aria-hidden="true"}Supported data types       | **Inputs**                                                                |
|                                               |                                                                           |
|                                               | Audio, video, text                                                        |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Output**                                                                |
|                                               |                                                                           |
|                                               | Audio and text                                                            |
|                                               | :::                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                                               |
| aria-hidden="true"}Token                      | **Input token limit**                                                     |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                                           |
|                                               | 128,000                                                                   |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Output token limit**                                                    |
|                                               |                                                                           |
|                                               | 8,000                                                                     |
|                                               | :::                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                                               |
| translate="no"}Capabilities                   | **Audio generation**                                                      |
|                                               |                                                                           |
|                                               | [Supported]{.gemini-api-supported}                                        |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Caching**                                                               |
|                                               |                                                                           |
|                                               | [Not supported]{.gemini-api-not-supported}                                |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Code execution**                                                        |
|                                               |                                                                           |
|                                               | [Not supported]{.gemini-api-not-supported}                                |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Function calling**                                                      |
|                                               |                                                                           |
|                                               | [Supported]{.gemini-api-supported}                                        |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Image generation**                                                      |
|                                               |                                                                           |
|                                               | [Not supported]{.gemini-api-not-supported}                                |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Search grounding**                                                      |
|                                               |                                                                           |
|                                               | [Supported]{.gemini-api-supported}                                        |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Structured outputs**                                                    |
|                                               |                                                                           |
|                                               | [Not supported]{.gemini-api-not-supported}                                |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Thinking**                                                              |
|                                               |                                                                           |
|                                               | [Supported]{.gemini-api-supported}                                        |
|                                               | :::                                                                       |
|                                               |                                                                           |
|                                               | ::: section                                                               |
|                                               | **Tuning**                                                                |
|                                               |                                                                           |
|                                               | [Not supported]{.gemini-api-not-supported}                                |
|                                               | :::                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                                               |
| aria-hidden="true"}Versions                   | Read the [model version                                                   |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) for more         |
|                                               | details.                                                                  |
|                                               |                                                                           |
|                                               | - Preview: `gemini-2.5-flash-preview-05-20`{translate="no" dir="ltr"}     |
|                                               | - Experimental:                                                           |
|                                               |   `gemini-2.5-flash-exp-native-audio-thinking-dialog`{translate="no"      |
|                                               |   dir="ltr"}                                                              |
|                                               | :::                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------+
| [calendar_month]{.google-symbols              | May 2025                                                                  |
| aria-hidden="true"}Latest update              |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+
| [cognition_2]{.google-symbols                 | January 2025                                                              |
| aria-hidden="true"}Knowledge cutoff           |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+
:::

::: section
### Gemini 2.5 Flash Image Preview {#gemini-2.5-flash-image-preview .showalways data-text="Gemini 2.5 Flash Image Preview" tabindex="-1"}

Gemini 2.5 Flash Image Preview is our latest, fastest, and most
efficient natively multimodal model that lets you generate and edit
images conversationally.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.5-flash-image-preview){.gemini-api-model-button}

#### Model details {#model-details_5 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.5-flash-image-preview`{translate="no"   |
| aria-hidden="true"}Model code                 | dir="ltr"}                                               |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Images and text                                          |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Images and text                                          |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 32,768                                                   |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 32,768                                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Not Supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Not Supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not Supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Not Supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Preview:                                               |
|                                               |   `gemini-2.5-flash-image-preview`{translate="no"        |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | August 2025                                              |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | June 2025                                                |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.5 Flash Preview Text-to-Speech {#gemini-2.5-flash-preview-tts .showalways data-text="Gemini 2.5 Flash Preview Text-to-Speech" tabindex="-1"}

Gemini 2.5 Flash Preview TTS is our price-performant text-to-speech
model, delivering high control and transparency for structured workflows
like podcast generation, audiobooks, customer support, and more. Gemini
2.5 Flash rate limits are more restricted since it is an experimental /
preview model.

[Try in Google AI
Studio](https://aistudio.google.com/generate-speech){.gemini-api-model-button}

#### Model details {#model-details_6 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.5-flash-preview-tts`{translate="no"     |
| aria-hidden="true"}Model code                 | dir="ltr"}                                               |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Audio                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 8,000                                                    |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 16,000                                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - `gemini-2.5-flash-preview-tts`{translate="no"          |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | May 2025                                                 |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.5 Pro Preview Text-to-Speech {#gemini-2.5-pro-preview-tts .showalways data-text="Gemini 2.5 Pro Preview Text-to-Speech" tabindex="-1"}

Gemini 2.5 Pro Preview TTS is our most powerful text-to-speech model,
delivering high control and transparency for structured workflows like
podcast generation, audiobooks, customer support, and more. Gemini 2.5
Pro rate limits are more restricted since it is an experimental /
preview model.

[Try in Google AI
Studio](https://aistudio.google.com/generate-speech){.gemini-api-model-button}

#### Model details {#model-details_7 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.5-pro-preview-tts`{translate="no"       |
| aria-hidden="true"}Model code                 | dir="ltr"}                                               |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Audio                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 8,000                                                    |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 16,000                                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - `gemini-2.5-pro-preview-tts`{translate="no" dir="ltr"} |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | May 2025                                                 |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.0 Flash {#gemini-2.0-flash .showalways data-text="Gemini 2.0 Flash" tabindex="-1"}

Gemini 2.0 Flash delivers next-gen features and improved capabilities,
including superior speed, native tool use, and a 1M token context
window.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.0-flash-001){.gemini-api-model-button}

#### Model details {#model-details_8 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.0-flash`{translate="no" dir="ltr"}      |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, images, video, and text                           |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Experimental]{.gemini-api-experimental}                 |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Batch Mode**                                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Latest: `gemini-2.0-flash`{translate="no" dir="ltr"}   |
|                                               | - Stable: `gemini-2.0-flash-001`{translate="no"          |
|                                               |   dir="ltr"}                                             |
|                                               | - Experimental: `gemini-2.0-flash-exp`{translate="no"    |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | February 2025                                            |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | August 2024                                              |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.0 Flash Preview Image Generation {#gemini-2.0-flash-preview-image-generation .showalways data-text="Gemini 2.0 Flash Preview Image Generation" tabindex="-1"}

Gemini 2.0 Flash Preview Image Generation delivers improved image
generation features, including generating and editing images
conversationally.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.0-flash-preview-image-generation){.gemini-api-model-button}

#### Model details {#model-details_9 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+-------------------------------------------------------------------+
| Property                                      | Description                                                       |
+===============================================+===================================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.0-flash-preview-image-generation`{translate="no" |
| aria-hidden="true"}Model code                 | dir="ltr"}                                                        |
+-----------------------------------------------+-------------------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                                       |
| aria-hidden="true"}Supported data types       | **Inputs**                                                        |
|                                               |                                                                   |
|                                               | Audio, images, video, and text                                    |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Output**                                                        |
|                                               |                                                                   |
|                                               | Text and images                                                   |
|                                               | :::                                                               |
+-----------------------------------------------+-------------------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                                       |
| aria-hidden="true"}Token                      | **Input token limit**                                             |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                                   |
|                                               | 32,000                                                            |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Output token limit**                                            |
|                                               |                                                                   |
|                                               | 8,192                                                             |
|                                               | :::                                                               |
+-----------------------------------------------+-------------------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                                       |
| translate="no"}Capabilities                   | **Structured outputs**                                            |
|                                               |                                                                   |
|                                               | [Supported]{.gemini-api-supported}                                |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Caching**                                                       |
|                                               |                                                                   |
|                                               | [Supported]{.gemini-api-supported}                                |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Tuning**                                                        |
|                                               |                                                                   |
|                                               | [Not supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Function calling**                                              |
|                                               |                                                                   |
|                                               | [Not supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Code execution**                                                |
|                                               |                                                                   |
|                                               | [Not Supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Search**                                                        |
|                                               |                                                                   |
|                                               | [Not Supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Image generation**                                              |
|                                               |                                                                   |
|                                               | [Supported]{.gemini-api-supported}                                |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Audio generation**                                              |
|                                               |                                                                   |
|                                               | [Not supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Live API**                                                      |
|                                               |                                                                   |
|                                               | [Not Supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
|                                               |                                                                   |
|                                               | ::: section                                                       |
|                                               | **Thinking**                                                      |
|                                               |                                                                   |
|                                               | [Not Supported]{.gemini-api-not-supported}                        |
|                                               | :::                                                               |
+-----------------------------------------------+-------------------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                                       |
| aria-hidden="true"}Versions                   | Read the [model version                                           |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) for more |
|                                               | details.                                                          |
|                                               |                                                                   |
|                                               | - Preview:                                                        |
|                                               |   `gemini-2.0-flash-preview-image-generation`{translate="no"      |
|                                               |   dir="ltr"}                                                      |
|                                               |                                                                   |
|                                               |   [gemini-2.0-flash-preview-image-generation is not currently     |
|                                               |   supported in a number of countries in Europe, Middle East &     |
|                                               |   Africa]{.gemini-api-not-supported}                              |
|                                               | :::                                                               |
+-----------------------------------------------+-------------------------------------------------------------------+
| [calendar_month]{.google-symbols              | May 2025                                                          |
| aria-hidden="true"}Latest update              |                                                                   |
+-----------------------------------------------+-------------------------------------------------------------------+
| [cognition_2]{.google-symbols                 | August 2024                                                       |
| aria-hidden="true"}Knowledge cutoff           |                                                                   |
+-----------------------------------------------+-------------------------------------------------------------------+
:::

::: section
### Gemini 2.0 Flash-Lite {#gemini-2.0-flash-lite .showalways data-text="Gemini 2.0 Flash-Lite" tabindex="-1"}

A Gemini 2.0 Flash model optimized for cost efficiency and low latency.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.0-flash-lite){.gemini-api-model-button}

#### Model details {#model-details_10 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.0-flash-lite`{translate="no" dir="ltr"} |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, images, video, and text                           |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Batch API**                                            |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Latest: `gemini-2.0-flash-lite`{translate="no"         |
|                                               |   dir="ltr"}                                             |
|                                               | - Stable: `gemini-2.0-flash-lite-001`{translate="no"     |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | February 2025                                            |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | August 2024                                              |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 2.0 Flash Live {#live-api-2.0 .showalways data-text="Gemini 2.0 Flash Live" tabindex="-1"}

The Gemini 2.0 Flash Live model works with the Live API to enable
low-latency bidirectional voice and video interactions with Gemini. The
model can process text, audio, and video input, and it can provide text
and audio output.

[Try in Google AI
Studio](https://aistudio.google.com?model=gemini-2.0-flash-live-001){.gemini-api-model-button}

#### Model details {#model-details_11 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-2.0-flash-live-001`{translate="no"        |
| aria-hidden="true"}Model code                 | dir="ltr"}                                               |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, video, and text                                   |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text, and audio                                          |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **Structured outputs**                                   |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Search**                                               |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Image generation**                                     |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Audio generation**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Thinking**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **URL context**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Preview: `gemini-2.0-flash-live-001`{translate="no"    |
|                                               |   dir="ltr"}                                             |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | April 2025                                               |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [cognition_2]{.google-symbols                 | August 2024                                              |
| aria-hidden="true"}Knowledge cutoff           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 1.5 Flash {#gemini-1.5-flash .showalways data-text="Gemini 1.5 Flash" tabindex="-1"}

Gemini 1.5 Flash is a fast and versatile multimodal model for scaling
across diverse tasks.

#### Model details {#model-details_12 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-1.5-flash`{translate="no" dir="ltr"}      |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, images, video, and text                           |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [movie_info]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Audio/visual specs         | **Maximum number of images per prompt**                  |
|                                               |                                                          |
|                                               | 3,600                                                    |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Maximum video length**                                 |
|                                               |                                                          |
|                                               | 1 hour                                                   |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Maximum audio length**                                 |
|                                               |                                                          |
|                                               | Approximately 9.5 hours                                  |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **System instructions**                                  |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **JSON mode**                                            |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **JSON schema**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Adjustable safety settings**                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Latest: `gemini-1.5-flash-latest`{translate="no"       |
|                                               |   dir="ltr"}                                             |
|                                               | - Latest stable: `gemini-1.5-flash`{translate="no"       |
|                                               |   dir="ltr"}                                             |
|                                               | - Stable:                                                |
|                                               |   - `gemini-1.5-flash-001`{translate="no" dir="ltr"}     |
|                                               |   - `gemini-1.5-flash-002`{translate="no" dir="ltr"}     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | [September 2025]{.gemini-api-not-supported}              |
| aria-hidden="true"}Deprecation date           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | September 2024                                           |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 1.5 Flash-8B {#gemini-1.5-flash-8b .showalways data-text="Gemini 1.5 Flash-8B" tabindex="-1"}

Gemini 1.5 Flash-8B is a small model designed for lower intelligence
tasks.

#### Model details {#model-details_13 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-1.5-flash-8b`{translate="no" dir="ltr"}   |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, images, video, and text                           |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 1,048,576                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [movie_info]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Audio/visual specs         | **Maximum number of images per prompt**                  |
|                                               |                                                          |
|                                               | 3,600                                                    |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Maximum video length**                                 |
|                                               |                                                          |
|                                               | 1 hour                                                   |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Maximum audio length**                                 |
|                                               |                                                          |
|                                               | Approximately 9.5 hours                                  |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **System instructions**                                  |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **JSON mode**                                            |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **JSON schema**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Adjustable safety settings**                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Latest: `gemini-1.5-flash-8b-latest`{translate="no"    |
|                                               |   dir="ltr"}                                             |
|                                               | - Latest stable: `gemini-1.5-flash-8b`{translate="no"    |
|                                               |   dir="ltr"}                                             |
|                                               | - Stable:                                                |
|                                               |   - `gemini-1.5-flash-8b-001`{translate="no" dir="ltr"}  |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | [September 2025]{.gemini-api-not-supported}              |
| aria-hidden="true"}Deprecation date           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | October 2024                                             |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

::: section
### Gemini 1.5 Pro {#gemini-1.5-pro .showalways data-text="Gemini 1.5 Pro" tabindex="-1"}

Try [Gemini 2.5 Pro
Preview](/gemini-api/docs/models/experimental-models#available-models),
our most advanced Gemini model to date.

Gemini 1.5 Pro is a mid-size multimodal model that is optimized for a
wide-range of reasoning tasks. 1.5 Pro can process large amounts of data
at once, including 2 hours of video, 19 hours of audio, codebases with
60,000 lines of code, or 2,000 pages of text.

#### Model details {#model-details_14 data-text="Model details" tabindex="-1"}

+-----------------------------------------------+----------------------------------------------------------+
| Property                                      | Description                                              |
+===============================================+==========================================================+
| [id_card]{.google-symbols                     | `models/gemini-1.5-pro`{translate="no" dir="ltr"}        |
| aria-hidden="true"}Model code                 |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [save]{.google-symbols                        | ::: section                                              |
| aria-hidden="true"}Supported data types       | **Inputs**                                               |
|                                               |                                                          |
|                                               | Audio, images, video, and text                           |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output**                                               |
|                                               |                                                          |
|                                               | Text                                                     |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [token_auto]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Token                      | **Input token limit**                                    |
| limits^[\[\*\]](#token-size){rel="footnote"}^ |                                                          |
|                                               | 2,097,152                                                |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Output token limit**                                   |
|                                               |                                                          |
|                                               | 8,192                                                    |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [movie_info]{.google-symbols                  | ::: section                                              |
| aria-hidden="true"}Audio/visual specs         | **Maximum number of images per prompt**                  |
|                                               |                                                          |
|                                               | 7,200                                                    |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Maximum video length**                                 |
|                                               |                                                          |
|                                               | 2 hours                                                  |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Maximum audio length**                                 |
|                                               |                                                          |
|                                               | Approximately 19 hours                                   |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [handyman]{.google-symbols aria-hidden="true" | ::: section                                              |
| translate="no"}Capabilities                   | **System instructions**                                  |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **JSON mode**                                            |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **JSON schema**                                          |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Adjustable safety settings**                           |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Caching**                                              |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Tuning**                                               |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Function calling**                                     |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Code execution**                                       |
|                                               |                                                          |
|                                               | [Supported]{.gemini-api-supported}                       |
|                                               | :::                                                      |
|                                               |                                                          |
|                                               | ::: section                                              |
|                                               | **Live API**                                             |
|                                               |                                                          |
|                                               | [Not supported]{.gemini-api-not-supported}               |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [123]{.google-symbols                         | ::: section                                              |
| aria-hidden="true"}Versions                   | Read the [model version                                  |
|                                               | patterns](/gemini-api/docs/models/gemini#model-versions) |
|                                               | for more details.                                        |
|                                               |                                                          |
|                                               | - Latest: `gemini-1.5-pro-latest`{translate="no"         |
|                                               |   dir="ltr"}                                             |
|                                               | - Latest stable: `gemini-1.5-pro`{translate="no"         |
|                                               |   dir="ltr"}                                             |
|                                               | - Stable:                                                |
|                                               |   - `gemini-1.5-pro-001`{translate="no" dir="ltr"}       |
|                                               |   - `gemini-1.5-pro-002`{translate="no" dir="ltr"}       |
|                                               | :::                                                      |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | [September 2025]{.gemini-api-not-supported}              |
| aria-hidden="true"}Deprecation date           |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
| [calendar_month]{.google-symbols              | September 2024                                           |
| aria-hidden="true"}Latest update              |                                                          |
+-----------------------------------------------+----------------------------------------------------------+
:::

See the [examples](/examples) to explore the capabilities of these model
variations.

\[\*\] A token is equivalent to about 4 characters for Gemini models.
100 tokens are about 60-80 English words.

## Model version name patterns {#model-versions data-text="Model version name patterns" tabindex="-1"}

Gemini models are available in either *stable*, *preview*, or
*experimental* versions. In your code, you can use one of the following
model name formats to specify which model and version you want to use.

### Latest stable {#latest-stable data-text="Latest stable" tabindex="-1"}

Points to the most recent stable version released for the specified
model generation and variation.

To specify the latest stable version, use the following pattern:
`<model>-<generation>-<variation>`{translate="no" dir="ltr"}. For
example, `gemini-2.0-flash`{translate="no" dir="ltr"}.

### Stable {#stable data-text="Stable" tabindex="-1"}

Points to a specific stable model. Stable models usually don\'t change.
Most production apps should use a specific stable model.

To specify a stable version, use the following pattern:
`<model>-<generation>-<variation>-<version>`{translate="no" dir="ltr"}.
For example, `gemini-2.0-flash-001`{translate="no" dir="ltr"}.

### Preview {#preview data-text="Preview" tabindex="-1"}

Points to a preview model which may not be suitable for production use,
come with more restrictive rate limits, but may have billing enabled.

To specify a preview version, use the following pattern:
`<model>-<generation>-<variation>-<version>`{translate="no" dir="ltr"}.
For example, `gemini-2.5-pro-preview-06-05`{translate="no" dir="ltr"}.

Preview models are not stable and availability of model endpoints is
subject to change.

### Experimental {#experimental data-text="Experimental" tabindex="-1"}

Points to an experimental model which may not be suitable for production
use and come with more restrictive rate limits. We release experimental
models to gather feedback and get our latest updates into the hands of
developers quickly.

To specify an experimental version, use the following pattern:
`<model>-<generation>-<variation>-<version>`{translate="no" dir="ltr"}.
For example, `gemini-2.0-pro-exp-02-05`{translate="no" dir="ltr"}.

Experimental models are not stable and availability of model endpoints
is subject to change.

## Experimental models {#experimental-models data-text="Experimental models" tabindex="-1"}

In addition to stable models, the Gemini API offers experimental models
which may not be suitable for production use and come with more
restrictive rate limits.

We release experimental models to gather feedback, get our latest
updates into the hands of developers quickly, and highlight the pace of
innovation happening at Google. What we learn from experimental launches
informs how we release models more widely. An experimental model can be
swapped for another without prior notice. We don\'t guarantee that an
experimental model will become a stable model in the future.

### Previous experimental models {#previous-experimental-models data-text="Previous experimental models" tabindex="-1"}

As new versions or stable releases become available, we remove and
replace experimental models. You can find the previous experimental
models we released in the following section along with the replacement
version:

  Model code                                                          Base model                    Replacement version
  ------------------------------------------------------------------- ----------------------------- -----------------------------------------------------------------------
  `gemini-embedding-exp-03-07`{translate="no" dir="ltr"}              Gemini Embedding              `gemini-embedding-001`{translate="no" dir="ltr"}
  `gemini-2.5-flash-preview-04-17`{translate="no" dir="ltr"}          Gemini 2.5 Flash              `gemini-2.5-flash-preview-05-20`{translate="no" dir="ltr"}
  `gemini-2.0-flash-exp-image-generation`{translate="no" dir="ltr"}   Gemini 2.0 Flash              `gemini-2.0-flash-preview-image-generation`{translate="no" dir="ltr"}
  `gemini-2.5-pro-preview-06-05`{translate="no" dir="ltr"}            Gemini 2.5 Pro                `gemini-2.5-pro`{translate="no" dir="ltr"}
  `gemini-2.5-pro-preview-05-06`{translate="no" dir="ltr"}            Gemini 2.5 Pro                `gemini-2.5-pro`{translate="no" dir="ltr"}
  `gemini-2.5-pro-preview-03-25`{translate="no" dir="ltr"}            Gemini 2.5 Pro                `gemini-2.5-pro`{translate="no" dir="ltr"}
  `gemini-2.0-flash-thinking-exp-01-21`{translate="no" dir="ltr"}     Gemini 2.5 Flash              `gemini-2.5-flash-preview-04-17`{translate="no" dir="ltr"}
  `gemini-2.0-pro-exp-02-05`{translate="no" dir="ltr"}                Gemini 2.0 Pro Experimental   `gemini-2.5-pro-preview-03-25`{translate="no" dir="ltr"}
  `gemini-2.0-flash-exp`{translate="no" dir="ltr"}                    Gemini 2.0 Flash              `gemini-2.0-flash`{translate="no" dir="ltr"}
  `gemini-exp-1206`{translate="no" dir="ltr"}                         Gemini 2.0 Pro                `gemini-2.0-pro-exp-02-05`{translate="no" dir="ltr"}
  `gemini-2.0-flash-thinking-exp-1219`{translate="no" dir="ltr"}      Gemini 2.0 Flash Thinking     `gemini-2.0-flash-thinking-exp-01-21`{translate="no" dir="ltr"}
  `gemini-exp-1121`{translate="no" dir="ltr"}                         Gemini                        `gemini-exp-1206`{translate="no" dir="ltr"}
  `gemini-exp-1114`{translate="no" dir="ltr"}                         Gemini                        `gemini-exp-1206`{translate="no" dir="ltr"}
  `gemini-1.5-pro-exp-0827`{translate="no" dir="ltr"}                 Gemini 1.5 Pro                `gemini-exp-1206`{translate="no" dir="ltr"}
  `gemini-1.5-pro-exp-0801`{translate="no" dir="ltr"}                 Gemini 1.5 Pro                `gemini-exp-1206`{translate="no" dir="ltr"}
  `gemini-1.5-flash-8b-exp-0924`{translate="no" dir="ltr"}            Gemini 1.5 Flash-8B           `gemini-1.5-flash-8b`{translate="no" dir="ltr"}
  `gemini-1.5-flash-8b-exp-0827`{translate="no" dir="ltr"}            Gemini 1.5 Flash-8B           `gemini-1.5-flash-8b`{translate="no" dir="ltr"}

## Supported languages {#supported-languages data-text="Supported languages" tabindex="-1"}

Gemini models are trained to work with the following languages:

- Arabic (`ar`{translate="no" dir="ltr"})
- Bengali (`bn`{translate="no" dir="ltr"})
- Bulgarian (`bg`{translate="no" dir="ltr"})
- Chinese simplified and traditional (`zh`{translate="no" dir="ltr"})
- Croatian (`hr`{translate="no" dir="ltr"})
- Czech (`cs`{translate="no" dir="ltr"})
- Danish (`da`{translate="no" dir="ltr"})
- Dutch (`nl`{translate="no" dir="ltr"})
- English (`en`{translate="no" dir="ltr"})
- Estonian (`et`{translate="no" dir="ltr"})
- Finnish (`fi`{translate="no" dir="ltr"})
- French (`fr`{translate="no" dir="ltr"})
- German (`de`{translate="no" dir="ltr"})
- Greek (`el`{translate="no" dir="ltr"})
- Hebrew (`iw`{translate="no" dir="ltr"})
- Hindi (`hi`{translate="no" dir="ltr"})
- Hungarian (`hu`{translate="no" dir="ltr"})
- Indonesian (`id`{translate="no" dir="ltr"})
- Italian (`it`{translate="no" dir="ltr"})
- Japanese (`ja`{translate="no" dir="ltr"})
- Korean (`ko`{translate="no" dir="ltr"})
- Latvian (`lv`{translate="no" dir="ltr"})
- Lithuanian (`lt`{translate="no" dir="ltr"})
- Norwegian (`no`{translate="no" dir="ltr"})
- Polish (`pl`{translate="no" dir="ltr"})
- Portuguese (`pt`{translate="no" dir="ltr"})
- Romanian (`ro`{translate="no" dir="ltr"})
- Russian (`ru`{translate="no" dir="ltr"})
- Serbian (`sr`{translate="no" dir="ltr"})
- Slovak (`sk`{translate="no" dir="ltr"})
- Slovenian (`sl`{translate="no" dir="ltr"})
- Spanish (`es`{translate="no" dir="ltr"})
- Swahili (`sw`{translate="no" dir="ltr"})
- Swedish (`sv`{translate="no" dir="ltr"})
- Thai (`th`{translate="no" dir="ltr"})
- Turkish (`tr`{translate="no" dir="ltr"})
- Ukrainian (`uk`{translate="no" dir="ltr"})
- Vietnamese (`vi`{translate="no" dir="ltr"})
::::::::::::::::::::::

Send feedback

::: devsite-floating-action-buttons
:::

Except as otherwise noted, the content of this page is licensed under
the [Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/), and code samples
are licensed under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0). For details, see
the [Google Developers Site
Policies](https://developers.google.com/site-policies). Java is a
registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-26 UTC.

::: devsite-content-data
Need to tell us more?

\[\[\[\"Easy to
understand\",\"easyToUnderstand\",\"thumb-up\"\],\[\"Solved my
problem\",\"solvedMyProblem\",\"thumb-up\"\],\[\"Other\",\"otherUp\",\"thumb-up\"\]\],\[\[\"Missing
the information I
need\",\"missingTheInformationINeed\",\"thumb-down\"\],\[\"Too
complicated / too many
steps\",\"tooComplicatedTooManySteps\",\"thumb-down\"\],\[\"Out of
date\",\"outOfDate\",\"thumb-down\"\],\[\"Samples / code
issue\",\"samplesCodeIssue\",\"thumb-down\"\],\[\"Other\",\"otherDown\",\"thumb-down\"\]\],\[\"Last
updated 2025-08-26 UTC.\"\],\[\],\[\],null,\[\]\]
:::
:::::::::::::::::::::::::::::::::
