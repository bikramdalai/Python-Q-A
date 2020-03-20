#Q1. Find all Words Strat with S?
import re
text = "bikram Sahoo 133434"
m = re.findall(r'[b]\w+', text)
print(str.join('', m))
