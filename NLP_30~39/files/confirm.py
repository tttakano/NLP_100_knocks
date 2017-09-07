import matplotlib.font_manager as fm

fonts = fm.findSystemFonts()
print([[str(font), fm.FontProperties(fname=font).get_name()] for font in fonts[:10]])
