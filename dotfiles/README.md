# scripts / dotfiles


## Vim

+ cp .vimrc ~/
+ open `vim`
  + use, depending on case: `:PluginInstall`, `:PluginUpdate`, `:PluginClean`


### Vim Devicons

Should use a patched font:
+ download specific font 
```bash
font_name="FiraCode"; curl -fLo ~/Downloads/$font_name.zip \
    https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/$font_name.zip
```
+ unzip and pipe to `/usr/share/fonts`
```bash
sudo sh -c 'font_name="FiraCode"; font_name_s="Fira Code" ; unzip -qq -c $font_name.zip "$font_name_s Regular Nerd Font Complete.otf" > /usr/share/fonts/opentype/"$font_name_s Regular Nerd Font Complete.otf"'
```

Note: Test with ~/Downloads/ before going to /usr/share/fonts/.

Note: Same for UbuntuMono:
```bash
font_name="UbuntuMono"; font_name_s="Ubuntu Mono" ; curl -fLo ~/Downloads/$font_name.zip \
    https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/$font_name.zip 

sudo sh -c 'font_name="UbuntuMono"; font_name_s="Ubuntu Mono" ; unzip -qq -c $font_name.zip "$font_name_s Nerd Font Complete.ttf" > /usr/share/fonts/truetype/"$font_name_s Nerd Font Complete.ttf"'
```
