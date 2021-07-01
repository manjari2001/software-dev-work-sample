"""A video player class."""

from video_library import VideoLibrary
from random import choice

playing = False
video_playing = None
paused = False

playlists = {}

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        all_videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        for video in all_videos:
            tag = str(video.tags).strip("()")
            print(f"{video.title} ({video.video_id}) [{tag}]")

    def play_video(self, video_id):
        """Plays the respective video."""
        all_videos = self._video_library.get_all_videos()
        video_ids = []
        for video in all_videos:
            video_ids.append(video.video_id)

        if video_id in video_ids:

            global playing
            global video_playing
            global paused

            if playing:
                print(f"Stopping video: {video_playing.title}")

            playing = True
            video_playing = self._video_library.get_video(video_id)

            print(f"Playing Video: {video_playing.title}")

            paused = False

        else:
            print("Cannot play video: video does not exist")


    def stop_video(self):
        """Stops the current video."""

        global playing
        global video_playing
        global paused

        if playing:
            print(f"Stopping video: {video_playing.title}")
            playing = False
            video_playing = None
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""

        all_videos = self._video_library.get_all_videos()
        videos = []
        for video in all_videos:
            videos.append(video.title)
        
        random_video = choice(videos)

        global playing
        global video_playing
        global paused

        if playing:
            print(f"Stopping video: {video_playing.title}")

        print(f"Playing video: {random_video}")

        paused = False

    def pause_video(self):
        """Pauses the current video."""

        global playing
        global video_playing
        global paused

        if playing and not paused:
            print(f"Pausing video: {video_playing.title}")
            paused = True
        elif paused:
            print(f"Video already paused: {video_playing.title}")
        elif not playing:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        global playing
        global video_playing
        global paused

        if paused:
            print(f"Continuing video: {video_playing.title}")
            paused = False
        elif playing and not paused:
            print("Cannot continue video: Video is not paused")
        elif not playing:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        global playing
        global video_playing
        global paused

        if playing:
            tag = str(video_playing.tags).strip("()")
            print(f"Currently playing: {video_playing.title} ({video_playing.video_id}) [{tag}])", end=" ")
            
            if paused:
                print("- Paused")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name."""

        global playlists

        already_exists = False

        for playlist in playlists:
            if playlist_name.lower == playlist.lower:
                print("Cannot create playlist: A playlist with the same name already exists")
                already_exists = True
            break

        if not already_exists:
            playlists[playlist_name] = []
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name."""

        global playlists

        playlist_exists = False

        all_videos = self._video_library.get_all_videos()
        videos = []
        for video in all_videos:
            videos.append(video.video_id)
        
        if video_id in videos:

            video = self._video_library.get_video(video_id)

            for playlist in playlists:

                if playlist_name.lower == playlist.lower:
                    if video in playlists[playlist]:
                        print(f"Cannot add video to {playlist}: Video already added")
                    else:    
                        playlists[playlist].append(video)
                        print(f"Added video to {playlist}: {video.title}")
                        playlist_exists = True
                        break

            if not playlist_exists:
                print(f"Cannot add video to {playlist_name}: Playlist does not exist")
                return
        else:
            print(f"Cannot add video to {playlist_name}: Video does not exist")


    def show_all_playlists(self):
        """Display all playlists."""

        global playlists

        if playlists:
            print("Showing all playlists:")
            for playlist in playlists:
                print(playlist)
        else:
            print("No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name."""

        playlist_exists = False

        for playlist in playlists:
            if playlist_name.lower == playlist.lower:
                print(f"Showing playlist: {playlist}")
                
                if len(playlists[playlist]) == 0:
                    print("No videos here yet")
                else:
                    for video in playlists[playlist]:
                        tag = str(video.tags).strip("()")
                        print(f"{video.title} ({video.video_id}) [{tag}]")
                
                playlist_exists = True

        if not playlist_exists:
            print(f"Cannot show {playlist_name}: Playlist does not exist")


    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name."""

        playlist_exists = False

        all_videos = self._video_library.get_all_videos()
        videos = []
        for video in all_videos:
            videos.append(video.video_id)
        
        if video_id in videos:

            video = self._video_library.get_video(video_id)

            for playlist in playlists:
                if playlist_name.lower == playlist.lower:
                    if video in playlists[playlist]:
                        playlists[playlist].remove(video)
                        print(f"Removed video from {playlist}: {video.title}")
                    else:
                        print(f"Cannot remove video from {playlist}: Video does not exist")

                    playlist_exists = True

            if not playlist_exists:
                print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
                return

        else:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name."""

        playlist_exists = False

        for playlist in playlists:
            if playlist_name.lower == playlist.lower:
                playlists[playlist] = []
                print(f"Successfully removed all videos from {playlist}")
                playlist_exists = True
        
        if not playlist_name:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")


    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name."""

        playlist_exists = False

        for playlist in playlists:
            if playlist_name.lower == playlist.lower:
                playlists.pop(playlist)
                print(f"Deleted playlist: my_playlist: {playlist}")
                playlist_exists = True
        
        if not playlist_name:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
