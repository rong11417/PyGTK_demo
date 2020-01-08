import pygtk
pygtk.require('2.0')
import gtk

class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("ComboBox with ListStore")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      
      combobox = gtk.ComboBox()
      store = gtk.ListStore(str)
      cell = gtk.CellRendererText()
      combobox.pack_start(cell)
      combobox.add_attribute(cell, 'text', 0)
      fixed = gtk.Fixed()
      lbl = gtk.Label("select a GUI toolkit")
      fixed.put(lbl, 25,75)
      fixed.put(combobox, 125,75)
      lbl2 = gtk.Label("Your choice is:")
      fixed.put(lbl2, 25,125)
      self.label = gtk.Label("")
      fixed.put(self.label, 125,125)
      self.add(fixed)
      
      store.append (["PyQt"])
      store.append (["Tkinter"])
      store.append (["WxPython"])
      store.append (["PyGTK"])
      store.append (["PySide"])
      combobox.set_model(store)
      combobox.connect('changed', self.on_changed)
      combobox.set_active(0)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
      return
   
   def on_changed(self, widget):
      self.label.set_label(widget.get_active_text())
      return
      
if __name__ == '__main__':

  PyApp()
  gtk.main()
