#################################
# Author: Ankit Murdia
# Created: 2017-12-14
# Updated: 
# Version: 1.0.0
# Description: Entry point for the Helpers package to list all the helpers that are part of this.
#################################

#--------- Dependencies ---------#
import os
import os.path
#--------------------------------#


#--------- CLI Handler ---------#
if __name__ == "__main__":
	dirpath = os.path.dirname(__file__)
	usage_list = []

	for f in os.listdir(dirpath):
		if not f.startswith("__") and not f.startswith("setting"):
			#module = "".join(f.split(".")[:-1]) # handles cases when a filename contains more than one "." eg. 20171210.error.log
			module = f.split(".")[0]
			desc = ""

			with open(os.path.join(dirpath, f), "r") as fp:
				for l in fp:
					if l.startswith("# Description:"):
						desc = "".join(l.split(":")[1:])
						break

			usage_list.append("{index}) {module}:\n\t\t{description}".format(index=len(usage_list) + 1, module=module, description=desc))

	print("\n#--------------------------- Helpers ---------------------------#\n\nBunch of very useful scripts that are designed to be used as modules in other projects but can of course be run independently when the need arises. Below is a list of all the helper modules that are part of this package:\n\n\t{content}".format(content="\n\t".join(usage_list)))
#-------------------------------#