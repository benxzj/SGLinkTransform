# SGLinkTransform
Transform complex Shotgun urls with entity detail anchors into direct links to detail pages

## Usage:
- `sg transform` - will transform a url in the clipboard from an anchored page into a direct detail page link.
- `sg transform` + `CMD` key - same as above, but will operate on the open tab of a browser in the foreground for Chrome, Safari, and probably Firefox (it's hacky)

## Page Types
There are multiple types of URLs in Shotgun and this tool helps with a few of them, namely:
- Page URLs:
    - https://somesite.shotgunstudio.com/page/4558
- Page URLs with entity detail anchors:
    - https://somesite.shotgunstudio.com/page/4558#Shot_1169_test
- Detail page URLs:
    - https://somesite.shotgunstudio.com/detail/Shot/1169

The first type of URL, the "page URL", shows a standard (possibly user created) page with entity record information.

The second type of URL, the "page URL with entity detail anchor", acts like an overlay of the page URL. When you click on a specific record link in a page URL to get detailed information, you will be redirected to an anchored page URL. This clicking of the link doesn't trigger a full page reload, but rather overlays the detail entity information "over" the previous view. This makes going back and forth between the list of entities and a single entity's details much more efficient. This could be considered an ancestor of modern single page web app systems.

The third type of URL is a "direct entity URL" that leads to the details of a single entity. Although this shows the same information as a page URL with an entity detail anchor, it is more efficient than the second type, _if_ you're storing it as a bookmark or sharing the link. It is more efficient because the page will only display the detail information, and never builds any of the background information that's involved when using an anchored page URL (multiple unseen records, etc).

## Some notes and tips:
- The `?layout=LayoutName` query parameter doesn't behave the same way on all three URL types:
    - page URL: `layout` refers to the views (or tabs) available on this page.
    - anchored page URL: the specified layout refers to views on the primary page URL (see above) and not the anchored view, which is unseen in the case of this view.
    - detail page: `layout` refers to possible views on the detail page
- CMD-clicking a specific record link in a page will bring you to a detail page inside a new tab instead of using the page with entity detail anchor optimization. You can also get to the detail link by right clicking on a link and choosing "Copy Link Address" from the menu.

## Release Notes:
- 1.0.0: Initial release
