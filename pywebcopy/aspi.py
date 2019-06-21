# save single page
# -----------------------------
from pywebcopy import save_webpage

kwargs = {'project_name': 'some-fancy-name3'}

save_webpage(
    url='http://example-site.com/index.html',
    project_folder='path/to/downloads',
    **kwargs
)

# save full website
# -----------------------------
# from pywebcopy import save_website

# kwargs = {'project_name': 'some-fancy-name'}

# save_website(
#     url='http://example-site.com/index.html',
#     project_folder='path/to/downloads',
#     **kwargs
# )


# -----------------------------
# replace **kwargs with this line if you got an AccessError; see readme for more information
# bypass_robots=True

