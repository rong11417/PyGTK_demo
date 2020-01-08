import gtk

class PyApp(gtk.Window):

   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Radio Button")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      vbox = gtk.VBox()
      
      btn1 = gtk.RadioButton(None, "Button 1")
      btn1.connect("toggled", self.on_selected)
      btn2 = gtk.RadioButton(btn1,"Button 2")
      btn2.connect("toggled", self.on_selected)
      btn3 = gtk.RadioButton(btn1,"Button 3")
      btn3.connect("toggled", self.on_selected)
      
      self.lbl = gtk.Label()
      vbox.add(btn1)
      vbox.add(btn2)
      vbox.add(btn3)
      vbox.add(self.lbl)
      self.add(vbox)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
   
   def on_selected(self, widget, data=None):
      self.lbl.set_text(widget.get_label()+" is selected")
if __name__ == '__main__':
   PyApp()
   gtk.main()
