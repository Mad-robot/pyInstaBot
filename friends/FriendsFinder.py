#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import pyInstaBot
from textblob import TextBlob
import time
import logging
import pyInstaBot.tools.strings as pystr
import pyInstaBot.instagram
import random


# Class to find new users to follow
class FriendsFinder(object):
    """
    Class to find new users to follow
    """

    # Constructor
    def __init__(self, hashtag="", shuffle=True, polarity=0.0, subjectivity=0.5, languages=['en']):
        """
        Constructor
        """
        # Properties
        self._hashtag = hashtag
        self._polarity = polarity
        self._subjectivity = subjectivity
        self._languages = languages

        # Feed
        self._users = pyInstaBot.instagram.InstagramConnector().hashtag_feed(hashtag)
        print(self._users)
        exit()
        self._users = self._users['ranked_items']

        # Shuffle
        if shuffle:
            random.shuffle(self._medias)
        # end if
    # end __init__

    #############################################
    # Override
    #############################################

    # Iterator
    def __iter__(self):
        """
        Iterator
        :return:
        """
        return self
    # end __iter__

    # Next
    def next(self):
        """
        Next element
        :return:
        """
        if len(self._medias) <= 0:
            raise StopIteration()
        # end if

        # Current media
        current_media = self._medias[0]

        # Remove
        self._medias.remove(current_media)

        # Return
        return current_media
    # end next

    # To unicode
    def __unicode__(self):
        """
        To unicode
        :return:
        """
        return u"FriendsFinder({})".format(self._search_keywords)
    # end __unicode__

    # To str
    def __str__(self):
        """
        To str
        :return:
        """
        return "FriendsFinder({})".format(self._search_keywords)
    # end __str__

    ############################################
    # Private
    ############################################

# end FriendsFinder
