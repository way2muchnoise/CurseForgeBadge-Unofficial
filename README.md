# CurseForgeBadge
A little badge/shield for minecraft mods/packs/... on CurseForge

## Usage
The base url is [https://cf.way2muchnoise.eu](https://cf.way2muchnoise.eu). Both http and https are available. 

**I advise using http when using it on GitHub since it doesn't seem to like my https that much.**

### Possible patterns

* /\<project>.svg: project being either the id or name(link in the url).
    * [![](http://cf.way2muchnoise.eu/240630.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/240630.svg`
    * [![](http://cf.way2muchnoise.eu/jei.svg)](https://minecraft.curseforge.com/projects/jei) -> `https://cf.way2muchnoise.eu/jei.svg`
* /\<style>\_\<project>_\<extra>.svg: style can either `short` or `full`, extra is optional text to be appended
    * [![](http://cf.way2muchnoise.eu/short_jei.svg)](https://minecraft.curseforge.com/projects/jei) -> `https://cf.way2muchnoise.eu/short_jei.svg`
    * [![](http://cf.way2muchnoise.eu/full_240630_downloads.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/full_240630_downloads.svg`
* /versions/\<project>.svg: project being either the id or name(link in the url).
    * [![](http://cf.way2muchnoise.eu/versions/jei.svg)](https://minecraft.curseforge.com/projects/jei) -> `https://cf.way2muchnoise.eu/versions/jei.svg`
    * [![](http://cf.way2muchnoise.eu/versions/240630.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/versions/240630.svg`
* /versions/\<text>\_\<project>\_\<style>.svg: text is optional and replaces the default `Available for` text. The style can be either `all` or `latest`
    * [![](http://cf.way2muchnoise.eu/versions/jei_latest.svg)](https://minecraft.curseforge.com/projects/jei) -> `https://cf.way2muchnoise.eu/versions/jei_latest.svg`
    * [![](http://cf.way2muchnoise.eu/versions/For%20MC_240630_all.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/versions/For%20MC_240630_all.svg`

For many more patterns see [https://cf.way2muchnoise.eu](https://cf.way2muchnoise.eu)
