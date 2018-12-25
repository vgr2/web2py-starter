db.define_table(
    'avatar',
    Field(
        'image',
        'string',
        length = 100,
    ),
    Field(
        'user_id',
        'reference auth_user',
        label=T('User'),
    ),
    auth.signature,
    singular = 'Avatar', plural = 'Avatars',
    format = '%(image)s',
)
