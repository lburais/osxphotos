# Test cloud photos

import pytest

PHOTOS_DB_CLOUD = "./tests/Test-Cloud-10.15.6.photoslibrary/database/photos.db"
PHOTOS_DB_NOT_CLOUD = "./tests/Test-10.15.6.photoslibrary/database/photos.db"

UUID_DICT = {
    "incloud": "37210110-E940-4227-92D3-45C40F68EB0A",
    "not_incloud": "33000A44-E4BA-43A3-9304-62A0195AB4D9",
    "cloudasset": "D11D25FF-5F31-47D2-ABA9-58418878DC15",
    "not_cloudasset": "6191423D-8DB8-4D4C-92BE-9BBBA308AAC4",
}


def test_incloud():
    import osxphotos

    photosdb = osxphotos.PhotosDB(PHOTOS_DB_CLOUD)
    photos = photosdb.photos(uuid=[UUID_DICT["incloud"]])

    assert photos[0].incloud


def test_not_incloud():
    import osxphotos

    photosdb = osxphotos.PhotosDB(PHOTOS_DB_CLOUD)
    photos = photosdb.photos(uuid=[UUID_DICT["not_incloud"]])

    assert not photos[0].incloud


def test_cloudasset_1():
    import osxphotos

    photosdb = osxphotos.PhotosDB(PHOTOS_DB_CLOUD)
    photos = photosdb.photos(uuid=[UUID_DICT["cloudasset"]])

    assert photos[0].iscloudasset


def test_cloudasset_2():
    import osxphotos

    photosdb = osxphotos.PhotosDB(PHOTOS_DB_CLOUD)
    photos = photosdb.photos(uuid=[UUID_DICT["not_incloud"]])

    # not_incloud is still a cloud asset
    assert photos[0].iscloudasset


def test_cloudasset_3():
    import osxphotos

    photosdb = osxphotos.PhotosDB(PHOTOS_DB_NOT_CLOUD)
    photos = photosdb.photos(uuid=[UUID_DICT["not_cloudasset"]])

    assert not photos[0].iscloudasset
