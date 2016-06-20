import sys
import git

def get_code(link):
	link = link.strip()
	args = link.split('/')
	folder = args[-2] + '_' + args[-1] + '/'
	# link = link[:-1] + '.git'
	link = link + '.git'

	print link
	# Repo.clone_from(link, '.', progress=None)
	git.Git().clone(link,'./codes/'+folder)


def main():
    file_in = open('links.txt', 'r')
    f = []
    for link in file_in:
    	if link in f:
    		pass
    	else:
    		get_code(link)
    		f.append(link)
    file_in.close()


if __name__ == "__main__":
    main()
