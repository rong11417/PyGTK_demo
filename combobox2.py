import gtk

class PyApp(gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Simple ComboBox")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      
      cb = gtk.combo_box_new_text()
      cb.connect("changed", self.on_changed)
      cb.append_text('PyQt')
      cb.append_text('Tkinter')
      cb.append_text('WxPython')
      cb.append_text('PyGTK')
      cb.append_text('PySide')
      
      fixed = gtk.Fixed()
      lbl = gtk.Label("select a GUI toolkit")
      fixed.put(lbl, 25,75)
      
      fixed.put(cb, 125,75)
      lbl2 = gtk.Label("Your choice is:")
      fixed.put(lbl2, 25,125)
      
      self.label = gtk.Label("")
      fixed.put(self.label, 125,125)
      self.add(fixed)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
   
   def on_changed(self, widget):
      self.label.set_label(widget.get_active_text())
if __name__ == '__main__':
   PyApp()
   gtk.main()
