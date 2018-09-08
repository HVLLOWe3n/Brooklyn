def upload_location_avatar(instance):
    """
    ####### For Model "User" #######

    Function for create location to upload avatar
    :param instance:
    :return: string.format
    """
    return "{}/{}/{}".format('Users', 'avatar', instance.username)
