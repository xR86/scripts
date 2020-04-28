" TODO
" * should start a Vim cheat sheet )eg: https://stackoverflow.com/a/4446090/6139015)
"
" Notes:
"* Install Vundle from https://github.com/VundleVim/Vundle.vim
"* After installing Vundle you have to call :PluginUpdate
"* if you want to keep a clean version of vim - https://stackoverflow.com/questions/9801360/install-multiple-version-of-vim-and-make-each-use-different-vimrc-file-respec
"
" Use:
" :PluginInstall
" :PluginUpdate
" :PluginClean
"
" Should use linting, similar to https://github.com/preservim/nerdcommenter/actions?workflow=Vint
" => based on https://github.com/Vimjas/vint
"
" Sidenote: Gnome Terminal has the zoom options as Ctrl + "+" and Ctrl + "-" 
" but it doesn't work with numpad plus/minus,
" remap again with the numpad even though it will look the same.
"
" Additional resources:
" * dotfiles / vimscript search on Github
" * https://www.youtube.com/watch?v=n9k9scbTuvQ
"

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" plugin on GitHub repo
" Plugin 'tpope/vim-fugitive'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'morhetz/gruvbox'
Plugin 'yggdroot/indentline'
Plugin 'preservim/nerdtree'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'airblade/vim-gitgutter'
" Plugin 'tiagofumo/vim-nerdtree-syntax-highlight' "too heavy scrolling time cost for NERDTree
Plugin 'ryanoasis/vim-devicons'

" Plugin 'majutsushi/tagbar'
" Plugin 'bronson/vim-trailing-whitespace'
" Plugin 'skywind3000/vim-terminal-help'

" Plugin 'sheerun/vim-polyglot'
" Plugin 'w0rp/ale'

" Plugin 'puremourning/vimspector'
" Plugin 'nvie/vim-flake8'
" Plugin 'klen/python-mode'
" Plugin 'tmhedberg/SimpylFold'

" Plugin 'wsdjeg/vim-todo'



" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

" ===================================================================================

" RULES
set number
set tabstop=4
"set ttyfast "fast scrolling
set smartindent

"syntax on
"syntax enable

" Show search results as typing
" inspired by: https://github.com/F1LT3R/dotfiles/blob/master/.vimrc
set incsearch
set showmatch
set hlsearch

" Color scheme
colorscheme gruvbox
set background=dark
let g:airline_theme='badwolf'

" Indent line
" let g:indentLine_setColors = 0
" let g:indentLine_color_term = 255
" let g:indentLine_bgcolor_term = 202
" let g:indentLine_bgcolor_gui = '#FF5F00'

" let g:indentLine_concealcursor = 'inc'
" let g:indentLine_conceallevel = 3

" let g:indentLine_char = '│'
" let g:indentLine_enabled=1

" NERDTree
autocmd vimenter * NERDTree
let g:WebDevIconsNerdTreeAfterGlyphPadding = ' '
" let NERDTreeShowHidden=1

highlight! link NERDTreeFlags NERDTreeDir
" colors current working directory (CWD)
highlight NERDTreeCWD ctermfg=white

" NERDTree Git - https://github.com/xuyuanp/nerdtree-git-plugin#faq
" the initial symbols might not make sense
" let g:NERDTreeIndicatorMapCustom = {}

"let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
let NERDTreeWinSize=40 "default 31
" let g:webdevicons_conceal_nerdtree_brackets = 1
" let g:WebDevIconsUnicodeDecorateFolderNodes = 1

" autoclose NERDTree if it's the only tab open
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Vim Devicons
let g:NERDTreeFileExtensionHighlightFullName = 1
"let g:NERDTreeExactMatchHighlightFullName = 1
let g:NERDTreePatternMatchHighlightFullName = 1

"let g:NERDTreeHighlightFolders = 1 " enables folder icon highlighting using exact match
"let g:NERDTreeHighlightFoldersFullName = 1 " highlights the folder name

" NERDTress File highlighting
function! NERDTreeHighlightFile(extension, fg, bg, guifg, guibg)
 exec 'autocmd filetype nerdtree highlight ' . a:extension .' ctermbg='. a:bg .' ctermfg='. a:fg .' guibg='. a:guibg .' guifg='. a:guifg
 exec 'autocmd filetype nerdtree syn match ' . a:extension .' #^\s\+.*'. a:extension .'$#'
endfunction

" Vim Devicons Fallback (source: https://github.com/preservim/nerdtree/issues/433#issuecomment-92590696)
"call NERDTreeHighlightFile('jade', 'green', 'none', 'green', '#151515')
"call NERDTreeHighlightFile('ini', 'yellow', 'none', 'yellow', '#151515')
call NERDTreeHighlightFile('md', 'blue', 'none', '#3366FF', '#151515')
"call NERDTreeHighlightFile('yml', 'yellow', 'none', 'yellow', '#151515')
"call NERDTreeHighlightFile('config', 'yellow', 'none', 'yellow', '#151515')
"call NERDTreeHighlightFile('conf', 'yellow', 'none', 'yellow', '#151515')
"call NERDTreeHighlightFile('json', 'yellow', 'none', 'yellow', '#151515')
"call NERDTreeHighlightFile('html', 'yellow', 'none', 'yellow', '#151515')
"call NERDTreeHighlightFile('styl', 'cyan', 'none', 'cyan', '#151515')
"call NERDTreeHighlightFile('css', 'cyan', 'none', 'cyan', '#151515')
"call NERDTreeHighlightFile('coffee', 'Red', 'none', 'red', '#151515')
"call NERDTreeHighlightFile('js', 'Red', 'none', '#ffa500', '#151515')
"call NERDTreeHighlightFile('php', 'Magenta', 'none', '#ff00ff', '#151515')


" Vim Syntax Highlight
let s:brown = "905532"
let s:aqua =  "3AFFDB"
let s:blue = "689FB6"
let s:darkBlue = "44788E"
let s:purple = "834F79"
let s:lightPurple = "834F79"
let s:red = "AE403F"
let s:beige = "F5C06F"
let s:yellow = "F09F17"
let s:orange = "D4843E"
let s:darkOrange = "F16529"
let s:pink = "CB6F6F"
let s:salmon = "EE6E73"
let s:green = "8FAA54"
let s:lightGreen = "31B53E"
let s:white = "FFFFFF"
let s:rspec_red = 'FE405F'
let s:git_orange = 'F54D27'

let g:NERDTreeExtensionHighlightColor = {} " this line is needed to avoid error
let g:NERDTreeExtensionHighlightColor['py'] = s:yellow " sets the color of css files to blue

let g:NERDTreeExactMatchHighlightColor = {} " this line is needed to avoid error
let g:NERDTreeExactMatchHighlightColor['.gitignore'] = s:git_orange " sets the color for .gitignore files

let g:NERDTreePatternMatchHighlightColor = {} " this line is needed to avoid error
let g:NERDTreePatternMatchHighlightColor['.*_spec\.rb$'] = s:rspec_red " sets the color for files ending with _spec.rb


"let g:WebDevIconsUnicodeDecorateFileNodes = 1
"autocmd filetype nerdtree highlight html_icon ctermbg=none ctermfg=Red guifg=#ffa500
"autocmd filetype nerdtree syn match html_icon ## containedin=NERDTreeFile,html

" Refresh vim-devicon
"if exists("g:loaded_webdevicons")
"	call webdevicons#refresh()
"endif
