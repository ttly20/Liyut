;;;;;;;;;;;;;;;;
;;Emacs基础配置;;
;;;;;;;;;;;;;;;;

;;关闭工具栏
(tool-bar-mode -1)
;;显示行号
(global-linum-mode t)
;;显示列号
(column-number-mode t)
;;行距
(setq line-spacing 4)
;;显示75列就换行
(setq default-fill-column 75)
(auto-fill-mode 1)
;;关闭滚动条
(scroll-bar-mode -1)
;;更改光标样式
(setq-default cursor-type 'bar)
;;关闭启动画面
(setq inhibit-startup-message t)
;;更改默认字体大小，24pt
(set-face-attribute 'default nil :height 240)
;;设置选择删除
(delete-selection-mode 1)
;;设置编码为UTF-8
(set-language-environment "UTF-8")
(setq default-buffer-file-coding-system 'utf-8)
;;快速打开配置文件函数
(defun open-init-file()
    (interactive)
    (find-file "~/.emacs.d/init.el"))
;;更改确认为y or n
(fset 'yes-or-no-p 'y-or-n-p)
;;默认全屏
(setq initial-frame-alist (quote ((fullscreen . maximized))))
;;以空行结束
(setq require-final-newline t)
;;默认开启txt-mode
(setq default-major-mode 'text-mode)
;;开启语法高亮
(global-font-lock-mode 1)
;;闪屏报警
(setq visible-bell t)
;;默认工作目录
(setq default-directory "~/Liyut")
;;撤销上限为200条操作
(setq kill-ring-max 200)
;;在标题栏上显示文件名
(setq frame-title-format "%n%F/%b")
;;设置个人信息
(setq user-full-name "Yue Li")
(setq user-mail-address "2750667 at qq.com")
;;缩进配置
(setq default-tab-width 4)
(setq-default indent-tabs-mode nil)
;;备份设置
(setq
    backup-by-copying t
    backup-directory-alist
	'(("." . "~/.saves"))
	delete-old-versions t
	kept-new-versions 6
	kept-old-versions 2
	version-control t)

;;;;;;;;;;;;;;;;;;
;;;;加载配置模块;;;;
;;;;;;;;;;;;;;;;;;

;;初始化配置模块位置
(package-initialize)
(add-to-list 'load-path "~/.emacs.d/lisp")
;;加载包管理
(require 'init-packages)
;;加载快捷键配置
(require 'my-Emacskbd)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(cfs--current-profile "profile1" t)
 '(cfs--profiles-steps (quote (("profile1" . 4))) t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
