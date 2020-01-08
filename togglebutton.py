import gtk

class PyApp(gtk.Window): 
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Toggle Button")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      
      vbox = gtk.VBox()
      self.btn1 = gtk.ToggleButton("Button 1")
      self.btn1.connect("toggled", self.on_toggled)
      self.btn2 = gtk.ToggleButton("Button 2")
      self.lbl = gtk.Label()
      
      vbox.add(self.btn1)
      vbox.add(self.btn2)
      vbox.add(self.lbl)
      self.add(vbox)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
   
   def on_toggled(self, widget, data = None):
      if self.btn1.get_active() == True:
         self.btn2.set_active(False)
      else:
         self.btn2.set_active(True)
         state = "Button1 : "+str(self.btn1.get_active())+"Button2 : "+str(self.btn2.get_active())
         self.lbl.set_text(state)
if __name__ == '__main__':
   PyApp()
   gtk.main()
