# CurseForgeBadge
A little badge/shield for minecraft mods/packs/... on CurseForge

## Usage
The base url is [https://cf.way2muchnoise.eu](https://cf.way2muchnoise.eu).
Both http and https are available.
 This url can be appended by following patterns.  

* /\<project>.svg: project being either the id or name(link in the url).
    * [![](https://cf.way2muchnoise.eu/240630.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/240630.svg`
    * [![](https://cf.way2muchnoise.eu/just-enough-items-jei.svg)](https://minecraft.curseforge.com/projects/just-enough-items-jei) -> `https://cf.way2muchnoise.eu/just-enough-items-jei.svg`
* /\<style>\_\<project>_\<extra>.svg: style can either `short` or `full`, extra is optional text to be appended
    * [![](https://cf.way2muchnoise.eu/short_just-enough-items-jei.svg)](https://minecraft.curseforge.com/projects/just-enough-items-jei) -> `https://cf.way2muchnoise.eu/short_just-enough-items-jei.svg`
    * [![](https://cf.way2muchnoise.eu/full_240630_downloads.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/full_240630_downloads.svg`
* /versions/\<project>.svg: project being either the id or name(link in the url).
    * [![](https://cf.way2muchnoise.eu/versions/just-enough-items-jei.svg)](https://minecraft.curseforge.com/projects/just-enough-items-jei) -> `https://cf.way2muchnoise.eu/versions/just-enough-items-jei.svg`
    * [![](https://cf.way2muchnoise.eu/versions/240630.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/versions/240630.svg`
* /versions/\<text>\_\<project>\_\<style>.svg: text is optional and replaces the default `Available for` text. The style can be either `all` or `latest`
    * [![](https://cf.way2muchnoise.eu/versions/just-enough-items-jei_latest.svg)](https://minecraft.curseforge.com/projects/just-enough-items-jei) -> `https://cf.way2muchnoise.eu/versions/just-enough-items-jei_latest.svg`
    * [![](https://cf.way2muchnoise.eu/versions/For%20MC_240630_all.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `https://cf.way2muchnoise.eu/versions/For%20MC_240630_all.svg`