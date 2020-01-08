import gtk

class PyApp(gtk.Window):
  def __init__(self):
    super(PyApp,self).__init__()
    self.set_title("Box demo")
    
    box=gtk.VBox()
    vb=gtk.VBox()

    lb1=gtk.Label("Enter name")
    vb.pack_start(lb1,expand=True,fill=True,padding=10)
    
    text=gtk.Entry()
    vb.pack_start(text,expand=True,fill=True,padding=10)
  
    btn=gtk.Button(stock=gtk.STOCK_OK)
    #btn=gtk.Button("hello")
    vb.pack_start(btn,expand=True,fill=True,padding=10)
    
    hb=gtk.HBox()
    lbl1=gtk.Label("Enter marks")
    hb.pack_start(lbl1,expand=True,fill=True,padding=5)
    
    text1=gtk.Entry()
    hb.pack_start(text1,expand=True,fill=True,padding=5)
  
    btn1=gtk.Button(stock=gtk.STOCK_SAVE)
    hb.pack_start(btn1,expand=True,fill=True,padding=5)
    
    box.add(vb)
    box.add(hb)
    self.add(box)
    
    self.show_all()

PyApp()
gtk.main()
