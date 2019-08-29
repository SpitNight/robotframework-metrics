from lxml import etree


class TopoParser():
	def __init__(self):
		self.filename="output.xml"
		self.dict_replacement={"Return: ":"", "b":"",",\n ":"\n", "\'":"", "(":"", ")":"", "IPv4Address":""}

	def parse(self):		
		tree = etree.parse(self.filename)
		return_values = tree.xpath(".//kw[@library='Collections'][./arguments/arg/text()='${dict_topo}']/msg[starts-with(text(), 'Return:')]")
		topo_info = return_values[-1].text
		for char, replacement in self.dict_replacement.iteritems():
			topo_info= topo_info.replace(char, replacement)
		topo_info_clean = topo_info[1:-1]
		return topo_info_clean