;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;插件管理配置;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(when (>= emacs-major-version 24)
    (require 'package)
    (package-initialize)
    (add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/") t))
;;cl-Common Lisp扩展
(require 'cl)
;;添加插件源与插件列表
(defvar Liyut_packages '(
			 ;;自动补全
			 company
			 js2-mode
			 nodejs-repl
			 yasnippet
			 cedet
			 ) "Default packages")
;;自动安装缺少的插件
(defun Liyut_packages_installed_p ()
    (loop for pkg in Liyut_packages
        when (not (package-installed-p pkg)) do (return nil)
	finally (return t)))
(unless (Liyut_packages_installed_p)
    (message "%s" "Refreshing package database...")
    (package-refresh-contents)
    (dolist (pkg Liyut_packages)
        (when (not (package-installed-p pkg))
	  (package-install pkg))))

;; 设置js2-mode到javascript文件
(setq auto-mode-alist
      (append
       '(("\\.js\\'" . js2-mode))
       auto-mode-alist))
;;打开补全功能
(global-company-mode t)

(require 'yasnippet)
(yas-reload-all t)
(add-hook 'prog-mode-hook #'yas-minor-mode)

(provide 'init-packages)
