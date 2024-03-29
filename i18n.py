#!/bin/env python
# coding: cp936

import os
import wx
import wx.xrc as xrc
import gettext

def install(app, localdir, languages):
    if app == None:
        gettext.install('hzdq', localedir = localdir, unicode = True)
    else:
        app.lang = wx.Locale()
        
        if languages[0] == 'zh_CN':
            app.lang.Init(wx.LANGUAGE_CHINESE_SIMPLIFIED)
        else:
            app.lang.Init(wx.LANGUAGE_DEFAULT)
        app.lang.AddCatalogLookupPathPrefix(localdir)
        app.lang.AddCatalog('hzdq')
        gettext.install('hzdq', localedir = localdir, unicode = True)

def install1(localdir, languages):
    lang = wx.Locale()
    
    if languages[0] == 'zh_CN':
        lang.Init(wx.LANGUAGE_CHINESE_SIMPLIFIED)
    else:
        lang.Init(wx.LANGUAGE_DEFAULT)
    lang.AddCatalogLookupPathPrefix(localdir)
    lang.AddCatalog('hzdq')
    gettext.install('hzdq', localedir=localdir, unicode=True)
    
if __name__ == '__main__':
    
    install(None,'lang',['zh_CN'])
    X =  _('hello')
    a = _('hello')
    print a
    print X
