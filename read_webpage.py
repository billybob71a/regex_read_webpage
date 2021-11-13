import requests
import re

link = "https://<web page>/page/2/?s=julia"

#since the webpage will give a sequence of paginations as page/<number>/?s=<search term
#I am going to use this as pattern seach to change the web link
pattern_page_number = r"(/)(?P<page_number>\d+)(/)"

match_page_number = re.search(pattern_page_number, link)

#uncomment the following if you want to find out how the grouping in regex worsk
# if match_page_number:
#     print("I found the whole match {}".format(match_page_number.group(0)))
#     print("I found the first group match {}".format(match_page_number.group(1)))
#     print("I found the second group match {}".format(match_page_number.group('page_number')))
#     print("I found the third group match {}".format(match_page_number.group(3)))


#I know that the pages go up to 12 as it's maximum so I listed the pages to '12' in list variable
replace = ['2', '3', '4', '5', '6', '7', '8', '9','10','11','12']

print("the page number is {}".format(match_page_number.group(2)))

# the function below replaced /<number>/ with the number of the page from the list variable, replace
# it will then put new generated url links into new url links
# these links will be placed into the list variabled called newlink


def replace_page_number(match_page_number, replace, link):
    newlinks = []
    for eachpage in replace:
        newlinks.append(re.sub(pattern_page_number, '/' + eachpage + '/', link))

    return newlinks


generated_links = replace_page_number(match_page_number, replace, link)
print("petery the new page number is {}".format(generated_links))


print("petery the new link is {}".format(generated_links))


pattern = r'((?i)(.*)Ninja)'

#in the function below , I am going to search the pattern that I am looking for from the ouput from f.text

for eachnew_link in generated_links:
    f = requests.get(eachnew_link)
    match = re.finditer(pattern, f.text)
    print("page is {}".format(eachnew_link))
    for eachitem in match:
        print("\t I found {} at index {}".format(eachitem.group(0), eachitem.start()))
