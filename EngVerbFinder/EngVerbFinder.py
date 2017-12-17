#EngVerbFinder.py
#Copyright (C) Yuhei Tohno
#the Author is available at: Y.Tohno [[atmark]] gmail.com
#the Author is in no event liable for any undesirable consequences from use of this package. 
"""
<Documentation>
This IronPython module provides a tiny GUI implementation for
a Part-Of-Speech Tagger function enshrined in Natural Language Toolkit
(NLTK), a natural language processing (NLP) library designed for
access from CPython scripting engine.
 
The present package, inclluding this module, is very simple,
but presumably unsimilar to typical NLTK-derived solutions.
 
Relying heavily on C extensions, NLTK does not seem to have met
any successful software interfaces channeling from the abundance
of NLP resources to other python implementations, e.g. IronPython 2.7.
 
Unlike CPython, IronPython can benefit from Windows Presentation Foundation
 (WPF) that shares many features with spick-and-span Windows technologies
to unleash the potential of modern PCs having graphic processing
offloaded from CPU to GPU.
 
This package offers an easy workaround that might suggest a bridge
between .NET(WPF) and NLTK in the corner of the universe ofPython programming.
 
Of plenty assets of WPF components, FlowDocumentReader may not be entitled
as the most popular one.
 
In fact, even Microsoft Visual Studio WPF toolbox doesn' t seem to support
automatic layout of this element (at least in default setting).
 
It is, however, a powerful GUI component affordable to host a FlowDocument
that can exploit most of the plethora of presentation interfaces defined
 in WPF.
 
FlowDocument, which is a XAML component, serves a crucial role in this package.
Because XAML is XML, you can deal with it by DOM manipulation,
file stream I/O or string processing.
 
This IronPython module invodes CPython scripting engine with an NLTK-
wrapper module contained in this package that works
around XML/text processing to discharge NLTK outputs.
  
The NLTK-output text strings (more precisely, items of a list) 
are in turn converted by CPython regular expression engine
to XAML-decorated code fragments to fill in as inner texts of a prescribed XML,
here XAML,  element, from which the WPF subsystem creates the flexible,
infographic document to dynamically dock in the WPF interface.
 
  
"""
import sys
import clr
clr.AddReference("PresentationFramework")
clr.AddReference("PresentationCore")
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Xml")
from System.Diagnostics import Process
from System.Windows.Forms import Clipboard as CB
from System.Windows.Forms import DataFormats
from System.IO import File
from System.Windows.Markup import XamlReader
from System.Windows import (
   Application, Window)
from System.Windows.Controls import (
   FlowDocumentReader)
from System.Xml import *


class EngVerbFinder(object):
    def __init__(self):
        documentReader = FlowDocumentReader()
        stream = File.OpenRead('EngVerbFinder_fdr.xaml')
        otree = XamlReader.Load(stream)
        self.Otree = otree
        self.DocumentReader =self.Otree.FindName("documentReader")
        self.Button1 = self.Otree.FindName("Button1")
        self.Button2 = self.Otree.FindName("Button2")
        self.Button3 = self.Otree.FindName("Button3")
        self.Button1.Click += self.Button1_Click
        self.Button2.Click += self.Button2_Click
        self.Button3.Click += self.Button3_Click
        self.Root = self.Otree.FindName("Grid1")
    def Button1_Click(self,sender,e):
        iData = CB.GetDataObject()
        if iData.GetDataPresent(DataFormats.Text):
            ctext = (iData.GetData(DataFormats.Text))
        if len(ctext) > 10000:
        	ctext = ctext[0:9999]          
        xmldoc = XmlDocument()
        xmldoc.Load('EngVerbFinder_fd_ipy.xaml')
        nsmgr = XmlNamespaceManager(xmldoc.NameTable)
        nsmgr.AddNamespace("xaml", "http://schemas.microsoft.com/winfx/2006/xaml/presentation")
        nsmgr.AddNamespace("x", "http://schemas.microsoft.com/winfx/2006/xaml/presentation")
        node1 = xmldoc.SelectSingleNode("/xaml:FlowDocument/xaml:Paragraph[@Name='First']",  nsmgr)
        node1.InnerText = ctext
        xmldoc.Save("EngVerbFinder_fd_ipy.xaml")
        self.DocumentReader.Document=XamlReader.Load(File.OpenRead('EngVerbFinder_fd_ipy.xaml'))
    def Button2_Click(self,sender,e):
        myprocess = Process.Start('C:\Python27\pythonw.exe', 'EngVerbFinder_POStag_module.py')
        myprocess.EnableRaisingEvents = True
        myprocess.WaitForExit()
        if myprocess.Exited:
        	self.DocumentReader.Document=XamlReader.Load(File.OpenRead('EngVerbFinder_fd_pos_tagged.xaml'))        
    def Button3_Click(self,sender,e):
    	#self.DocumentReader.Document=XamlReader.Load(File.OpenRead('EngVerbFinder_fd_pos_tagged.xaml'))
        self.DocumentReader.Document=XamlReader.Load(File.OpenRead('EngVerbFinder_fd_ipy.xaml'))
        
        
if __name__ == '__main__':
    fd = EngVerbFinder()
    window = Window()
    window.Title ="EngVerbFinder"
    window.Height=400
    window.Width=500
    window.Content = fd.Root
    app = Application()
    app.Run(window)