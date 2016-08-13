;;define the base path
(defvar plugin-path "~/.emacs.d/plugins")
(defvar config-path "~/.emacs.d/my-config")
(defvar temp-path "~/.emacs.d/temp")
(defvar plugin-config-path (concat config-path "/plugin-config"))
(defvar elisp-fun-path (concat config-path "/elisp-fun"))


;;定义待安装的插件列表，这个值是 M-x list-package 中列出的名字
(setq jpk-package-list
'(


;;=========================================IN USED PKG ====================================================
auto-complete ;; 代码自动补全
yasnippet ;; 代码自动补全
cedet ;; 代码跳转

;;========================================================================================================






;;=========================================NOT IN USE ====================================================
;; emacs-setup ;; help to setup emacs and customize variables
;; slime ;; common-lisp support
;; git ;; git support
;; f ;; dependency package for git
;; s ;; dependency package for git
;;========================================================================================================


))
