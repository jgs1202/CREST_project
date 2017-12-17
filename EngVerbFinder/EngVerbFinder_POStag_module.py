import nltk
import re
import codecs
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

class VerbFinder(object):
    front_half = """
        <FlowDocument xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
        <Paragraph Name="First" FontSize="14">
        """
    rear_half = """ 
       </Paragraph>
    </FlowDocument>
          """
    def postagging(self):
        try:
            tree = ET.parse('EngVerbFinder_fd_ipy.xaml')
            root = tree.getroot()
            raw = root.find(".//{http://schemas.microsoft.com/winfx/2006/xaml/presentation}Paragraph[@Name='First']").text  
            pos = nltk.pos_tag(nltk.word_tokenize(raw))
            pos = sorted(list(set(pos)), key=pos.index)
            front_tag = ' <Run Foreground="Red" TextDecorations="Underline"> '
            rear_tag = ' </Run> '
            pos_tagged = raw
            pos_tagged = escape(pos_tagged)
            fipos = [str(p[0]) for p in pos if str(p[1]).find("VB") > -1]
            fipos = sorted(list(set(fipos)), key=fipos.index)
            for fp in fipos:
                fp = " " + fp + " "
                taggedstrp = front_tag + fp + rear_tag
                pos_tagged= re.sub(re.escape(fp), taggedstrp, pos_tagged, count=0)
            whole = self.front_half + pos_tagged + self.rear_half
            codecs.register_error('strict', codecs.replace_errors)
            try:
                outputfile = codecs.open('EngVerbFinder_fd_pos_tagged.xaml', 'w+', 'utf-8', 'strict').write(codecs.encode(whole, 'utf-8'))            
            except:
                self.errorHandller()
        except:
            self.errorHandller()
    
    
    def errorHandller(self):
                outputfile = open('EngVerbFinder_fd_pos_tagged.xaml', 'w+')
                er = self.front_half + "ERROR: Check and remove if any non-utf-8 characters are contained in your clipboard text." + self.rear_half
                outputfile.write(er)
                outputfile.close()

if __name__ == '__main__': 
    VerbFinder().postagging()
