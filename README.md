# Logos Ecosystem Wiki

Logos Ecosystem related information.

While this repository is currently *private*, it may be set to **public** in the future.
Do not commit sensitive information that must never be published in this repo.

## CI / CD

None for now. If setup, should use auth.

## Using Obsidian

Quartz is created to serve a static site off of an [Obsidian](https://obsidian.md) vault, and thus is the preferred way to manage content locally. In order for all it to function properly, a few things need to be done properly.

First and foremost, Quartz uses links references with `content` as the root directory, so when opening in Obsidian, open the `content` folder, and _not_ the repo directory.

Then the following vault settings need to be configured

- under `Options --> Files and Links`
  - enable `Automatically update internal links`
  - `Link format` should be set to `Absolute path in vault`
  - enable `use Wikilinks`

In order to use the templates in the `Templates` folder for auto populating commmon files,

- Install and enable `Templater` in the Community Plugins
  - set the `Templates folder` to `templates`
  - enable `automatic jump to cursor`
  - enable `Trigger Templater on new file creation`
  - enable `Folder templates`
  - assign whichever templates you want to be triggered when a new file is created in a given folder.

Refer the [Templater documentation](https://silentvoid13.github.io/Templater/) for how to create your own templates.

## Local development

Run locally with live refresh:

```bash
npx quartz build --serve
```
