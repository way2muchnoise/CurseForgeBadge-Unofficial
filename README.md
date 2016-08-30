# CurseForgeBadge
A little badge/shield for minecraft mods/packs/... on CurseForge

## Usage
The base url is [http://cf.way2muchnoise.eu](http://cf.way2muchnoise.eu). This url can be appended by following patterns.

* /\<project>.svg: project being either the id or name(link in the url).
    * [![](http://cf.way2muchnoise.eu/240630.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `http://cf.way2muchnoise.eu/240630.svg`
    * [![](http://cf.way2muchnoise.eu/just-enough-items-jei.svg)](https://minecraft.curseforge.com/projects/just-enough-items-jei) -> `http://cf.way2muchnoise.eu/just-enough-items-jei.svg`
* /\<style>\_\<project>_\<extra>.svg: style can either `short` or `full`, extra is optional text to be appended
    * [![](http://cf.way2muchnoise.eu/short_just-enough-items-jei.svg)](https://minecraft.curseforge.com/projects/just-enough-items-jei) -> `http://cf.way2muchnoise.eu/short_just-enough-items-jei.svg`
    * [![](http://cf.way2muchnoise.eu/full_240630_downloads.svg)](https://minecraft.curseforge.com/projects/just-enough-resources-jer) -> `http://cf.way2muchnoise.eu/full_240630_downloads.svg`