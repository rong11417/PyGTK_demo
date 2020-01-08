import gtk

class PyApp(gtk.Window):

   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("Toolbar Demo")
      self.set_default_size(250, 200)
      self.set_position(gtk.WIN_POS_CENTER)
      
      toolbar = gtk.Toolbar()
      toolbar.set_style(gtk.TOOLBAR_ICONS)
      toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)
      
      newbtn = gtk.ToolButton(gtk.STOCK_NEW)
      newbtn.set_tooltip_text("New")
      openbtn = gtk.ToolButton(gtk.STOCK_OPEN)
      savebtn = gtk.ToolButton(gtk.STOCK_SAVE)
      sep = gtk.SeparatorToolItem()
      
      rb1 = gtk.RadioToolButton(None,gtk.STOCK_JUSTIFY_LEFT)
      53
      rb2 = gtk.RadioToolButton(rb1,gtk.STOCK_JUSTIFY_RIGHT)
      
      prv = gtk.ToggleToolButton(gtk.STOCK_PRINT_PREVIEW)
      quitbtn = gtk.ToolButton(gtk.STOCK_QUIT)
      
      toolbar.insert(newbtn, 0)
      toolbar.insert(openbtn, 1)
      toolbar.insert(savebtn, 2)
      toolbar.insert(sep, 3)
      toolbar.insert(rb1,4)
      toolbar.insert(rb2,5)
      toolbar.insert(prv,6)
      toolbar.insert(quitbtn, 7)
      
      quitbtn.connect("clicked", gtk.main_quit)
      vbox = gtk.VBox(False, 2)
      vbox.pack_start(toolbar, False, False, 0)
      
      self.add(vbox)
      self.connect("destroy", gtk.main_quit)
      self.show_all()
   
   def on_checked(self, widget, data = None):
      state = "Button1 : "+str(self.btn1.get_active())+"Button2 : "+str(self.btn2.get_active())
      self.lbl.set_text(state)
if __name__ == '__main__':
   PyApp()
   gtk.main()
