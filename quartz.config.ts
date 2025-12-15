import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Logos Ecosystem Development",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-GB",
    baseUrl: "ecosystem.logos.co",
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#FAFAFA", // Soft off-white background
          lightgray: "#E8E8E8", // Soft light gray for subtle sections
          gray: "#9AB5C7", // Muted blue-gray
          darkgray: "#4A4A4A", // Soft dark gray for body text
          dark: "#1A1A1A", // Soft black for headers
          secondary: "#5570E3", // Softened blue (muted from #001AFF)
          tertiary: "#E6A87C", // Softened orange (muted from #FD9937)
          highlight: "rgba(85, 112, 227, 0.08)", // Very subtle blue highlight
          textHighlight: "rgba(230, 168, 124, 0.15)", // Soft orange text highlight
        },
        darkMode: {
          light: "#232b2b", // Soft black background (not pure black)
          lightgray: "#1C1C1E", // Soft dark gray for cards/sections
          gray: "#5A5A5A", // Muted gray for secondary elements
          darkgray: "#C5C5C7", // Soft light gray for body text
          dark: "#E8E8EA", // Soft white for headers (not pure white)
          secondary: "#7A8FE8", // Soft blue accent for dark mode
          tertiary: "#D4A574", // Soft orange/amber accent
          highlight: "rgba(122, 143, 232, 0.12)", // Subtle blue highlight
          textHighlight: "rgba(212, 165, 116, 0.18)", // Soft orange highlight
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      // Plugin.CustomOgImages(),
    ],
  },
}

export default config
