import gtk

class PyApp(gtk.Window):
  def __init__(self):
      
    super(PyApp, self).__init__()
    self.set_title("Menu Demo")
    self.set_default_size(500, 450)
    self.set_position(gtk.WIN_POS_CENTER)
      
    mb = gtk.MenuBar()
      
    menu1 = gtk.Menu()
    file = gtk.MenuItem("_File")
    file.set_submenu(menu1)
    acgroup = gtk.AccelGroup()
    self.add_accel_group(acgroup)
    new = gtk.ImageMenuItem(gtk.STOCK_NEW,acgroup)
    new.add_accelerator("activate", acgroup, ord('N'), 
    gtk.gdk.CONTROL_MASK, gtk.ACCEL_VISIBLE)
      
    menu1.append(new)
    open = gtk.ImageMenuItem(gtk.STOCK_OPEN)
      
    menu1.append(open)
    chk = gtk.CheckMenuItem("Checkable")
      
    menu1.append(chk)
    radio1 = gtk.RadioMenuItem(None,"Radio1")
    radio2 = gtk.RadioMenuItem(radio1, "Radio2")
      
    menu1.append(radio1)
    menu1.append(radio2)
    sep = gtk.SeparatorMenuItem()
      
    menu1.append(sep)
    exit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
      
    menu1.append(exit)
    menu2 = gtk.Menu()
    edit = gtk.MenuItem("_Edit")
    edit.set_submenu(menu2)
    copy = gtk.ImageMenuItem(gtk.STOCK_COPY)
      
    menu2.append(copy)
    cut = gtk.ImageMenuItem(gtk.STOCK_CUT)
      
    menu2.append(cut)
    paste = gtk.ImageMenuItem(gtk.STOCK_PASTE)
      
    menu2.append(paste)
    mb.append(file)
    mb.append(edit)
    vbox = gtk.VBox(False, 2)
    vbox.pack_start(mb, False, False, 0)
      
    self.add(vbox)
    self.connect("destroy", gtk.main_quit)
    self.show_all()
if __name__ == '__main__':
  PyApp()
  gtk.main()
