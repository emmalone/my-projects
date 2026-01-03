---
title: "cards"
project: klm-plan
original_path: themes/hugo-book/exampleSite/content.en/docs/shortcodes/experimental/cards.md
modified: 2026-01-02T22:53:12.758646
---

# Cards

> [!WARNING]
> Experimental, could change in the future or be removed

## Example

{{% columns %}}
- {{< card image="placeholder.svg" >}}
  ### Line 1
  Line 2
  {{< /card >}}

- {{< card image="placeholder.svg" >}}
  This is tab MacOS content.
  {{< /card >}}
{{% /columns %}}

{{% columns %}}
- {{< card href="/docs/shortcodes/experimental/cards" >}}
  **Markdown**  
  Suspendisse sed congue orci, eu congue metus. Nullam feugiat urna massa.
  {{< /card >}}

- {{< card >}}
  Suspendisse sed congue orci, eu congue metus. Nullam feugiat urna massa, et fringilla metus consectetur molestie.
  {{< /card >}}

- {{< card title="Card" >}}
  ### Heading
  This is tab MacOS content.
  {{< /card >}}
{{% /columns %}}
