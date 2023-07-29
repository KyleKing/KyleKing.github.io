# SoundCloud Generator

## Summary

I listen to SoundCloud all the time and wanted to shuffle and generate new playlists, but SoundCloud didn't offer those features natively. Using the SoundCloud API, I built a Python CLI tool to create and update playlists based on custom parameters

## How's it work?

To allow you to work with re-posted tracks (not part of the API), I had to create a separate account that only follows my main account. With this workaround, the second account's entire activity feed is filled with re-posted songs by my main account, which I can fetch with the SoundCloud API. From the fetched songs, I can generate playlists for most commented, genre, tag, date released, etc.

Users can clone the project, setup their profile information in a settings file, then quickly generate playlists to their own account. To see how to take advantage of the tool and generate your own playlists, visit the [Github repository](https://github.com/KyleKing/soundcloud_playlist_maker)

Sample CLI Output:

![TBD](./imgs/SoundCloud/terminal.png)
