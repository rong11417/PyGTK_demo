import gtk
import pango

class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Dialog Boxes")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      
      mb = gtk.MenuBar()
      menu1 = gtk.Menu()
      file = gtk.MenuItem("_File")
      file.set_submenu(menu1)
      msg = gtk.MenuItem("MessageDialog")
      
      menu1.append(msg)
      abt = gtk.MenuItem("AboutDialog")
      menu1.append(abt)
      colo = gtk.MenuItem("colorDialog")
      menu1.append(colo)
      font = gtk.MenuItem("FontSelectionDialog")
      menu1.append(font)
      fl = gtk.MenuItem("FileChooserDialog")
      menu1.append(fl)
      mb.append(file)
      
      vbox = gtk.VBox(False, 2)
      vbox.pack_start(mb, False, False, 0)
      self.add(vbox)
      self.text = gtk.Label("TutorialsPoint")
      vbox.pack_start(self.text, True, True, 0)
      #msg.connect("activate",self.on_msgdlg)
      #abt.connect("activate",self.on_abtdlg)
      #font.connect("activate",self.on_fntdlg)
      #colo.connect("activate",self.on_color)
      
      #fl.connect("activate", self.on_file)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
      #def on_msgdlg(self,widget):
      #...
      #def on_abtdlg(self,widget):
      #...
      #def on_fntdlg(self,widget):
      #...
      #def on_color(self, widget):
      #...
      #def on_file(self, widget):
      #...
if __name__ == '__main__':
   PyApp()
   gtk.main()
