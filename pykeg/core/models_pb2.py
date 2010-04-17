# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='core/models.proto',
  package='',
  serialized_pb='\n\x11\x63ore/models.proto\"%\n\tBeerStyle\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\"\xba\x01\n\x08\x42\x65\x65rType\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x11\n\tbrewer_id\x18\x03 \x02(\r\x12\x17\n\x06\x62rewer\x18\x04 \x01(\x0b\x32\x07.Brewer\x12\x10\n\x08style_id\x18\x05 \x02(\r\x12\x19\n\x05style\x18\x06 \x01(\x0b\x32\n.BeerStyle\x12\x16\n\x0b\x63\x61lories_oz\x18\x07 \x02(\x02:\x01\x30\x12\x13\n\x08\x63\x61rbs_oz\x18\x08 \x02(\x02:\x01\x30\x12\x0e\n\x03\x61\x62v\x18\t \x02(\x02:\x01\x30\"\x83\x01\n\x06\x42rewer\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x18\n\x0eorigin_country\x18\x03 \x02(\t:\x00\x12\x16\n\x0corigin_state\x18\x04 \x02(\t:\x00\x12\x15\n\x0borigin_city\x18\x05 \x02(\t:\x00\x12\x16\n\x0c\x64istribution\x18\x06 \x02(\t:\x00\"\xba\x01\n\x05\x44rink\x12\n\n\x02id\x18\x01 \x02(\r\x12\r\n\x05ticks\x18\x02 \x02(\r\x12\x11\n\tvolume_ml\x18\x03 \x02(\x02\x12\x11\n\tstarttime\x18\x04 \x02(\x07\x12\x0f\n\x07\x65ndtime\x18\x05 \x02(\x07\x12\x16\n\x08is_valid\x18\x06 \x02(\x08:\x04true\x12\x0e\n\x06keg_id\x18\x07 \x01(\r\x12\x11\n\x03keg\x18\x08 \x01(\x0b\x32\x04.Keg\x12\x0f\n\x07user_id\x18\t \x02(\t\x12\x13\n\x04user\x18\n \x01(\x0b\x32\x05.User\"\xaf\x01\n\x03Keg\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0f\n\x07type_id\x18\x02 \x02(\r\x12\x17\n\x04type\x18\x03 \x01(\x0b\x32\t.BeerType\x12\x0f\n\x07size_id\x18\x04 \x02(\r\x12\x16\n\x04size\x18\x05 \x01(\x0b\x32\x08.KegSize\x12\x11\n\tstartdate\x18\x06 \x02(\x07\x12\x0f\n\x07\x65nddate\x18\x07 \x02(\x07\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x10\n\x08origcost\x18\t \x01(\x02\"6\n\x07KegSize\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x11\n\tvolume_ml\x18\x03 \x02(\x02\"j\n\x06KegTap\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x16\n\x0e\x63urrent_keg_id\x18\x05 \x01(\r\x12\x19\n\x0b\x63urrent_keg\x18\x06 \x01(\x0b\x32\x04.Keg\"\xac\x01\n\x04User\x12\x10\n\x08username\x18\x01 \x02(\t\x12\x17\n\tis_active\x18\x02 \x02(\x08:\x04true\x12\x13\n\x0bmugshot_url\x18\x03 \x01(\t\x12\x19\n\nis_unknown\x18\x04 \x02(\x08:\x05\x66\x61lse\x12\x17\n\x08is_staff\x18\x05 \x02(\x08:\x05\x66\x61lse\x12\x1b\n\x0cis_superuser\x18\x06 \x02(\x08:\x05\x66\x61lse\x12\x13\n\x0b\x64\x61te_joined\x18\x07 \x02(\x07')




_BEERSTYLE = descriptor.Descriptor(
  name='BeerStyle',
  full_name='BeerStyle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='BeerStyle.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='BeerStyle.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=21,
  serialized_end=58,
)


_BEERTYPE = descriptor.Descriptor(
  name='BeerType',
  full_name='BeerType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='BeerType.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='BeerType.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='brewer_id', full_name='BeerType.brewer_id', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='brewer', full_name='BeerType.brewer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='style_id', full_name='BeerType.style_id', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='style', full_name='BeerType.style', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='calories_oz', full_name='BeerType.calories_oz', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='carbs_oz', full_name='BeerType.carbs_oz', index=7,
      number=8, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='abv', full_name='BeerType.abv', index=8,
      number=9, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=61,
  serialized_end=247,
)


_BREWER = descriptor.Descriptor(
  name='Brewer',
  full_name='Brewer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Brewer.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='Brewer.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origin_country', full_name='Brewer.origin_country', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origin_state', full_name='Brewer.origin_state', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origin_city', full_name='Brewer.origin_city', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='distribution', full_name='Brewer.distribution', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=250,
  serialized_end=381,
)


_DRINK = descriptor.Descriptor(
  name='Drink',
  full_name='Drink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Drink.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ticks', full_name='Drink.ticks', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='volume_ml', full_name='Drink.volume_ml', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='starttime', full_name='Drink.starttime', index=3,
      number=4, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='endtime', full_name='Drink.endtime', index=4,
      number=5, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_valid', full_name='Drink.is_valid', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keg_id', full_name='Drink.keg_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keg', full_name='Drink.keg', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_id', full_name='Drink.user_id', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user', full_name='Drink.user', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=384,
  serialized_end=570,
)


_KEG = descriptor.Descriptor(
  name='Keg',
  full_name='Keg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='Keg.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type_id', full_name='Keg.type_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='Keg.type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size_id', full_name='Keg.size_id', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='Keg.size', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='startdate', full_name='Keg.startdate', index=5,
      number=6, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enddate', full_name='Keg.enddate', index=6,
      number=7, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='Keg.description', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origcost', full_name='Keg.origcost', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=573,
  serialized_end=748,
)


_KEGSIZE = descriptor.Descriptor(
  name='KegSize',
  full_name='KegSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='KegSize.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='KegSize.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='volume_ml', full_name='KegSize.volume_ml', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=750,
  serialized_end=804,
)


_KEGTAP = descriptor.Descriptor(
  name='KegTap',
  full_name='KegTap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='KegTap.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='KegTap.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='KegTap.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='current_keg_id', full_name='KegTap.current_keg_id', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='current_keg', full_name='KegTap.current_keg', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=806,
  serialized_end=912,
)


_USER = descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_active', full_name='User.is_active', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mugshot_url', full_name='User.mugshot_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_unknown', full_name='User.is_unknown', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_staff', full_name='User.is_staff', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_superuser', full_name='User.is_superuser', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='date_joined', full_name='User.date_joined', index=6,
      number=7, type=7, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=915,
  serialized_end=1087,
)


_BEERTYPE.fields_by_name['brewer'].message_type = _BREWER
_BEERTYPE.fields_by_name['style'].message_type = _BEERSTYLE
_DRINK.fields_by_name['keg'].message_type = _KEG
_DRINK.fields_by_name['user'].message_type = _USER
_KEG.fields_by_name['type'].message_type = _BEERTYPE
_KEG.fields_by_name['size'].message_type = _KEGSIZE
_KEGTAP.fields_by_name['current_keg'].message_type = _KEG

class BeerStyle(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BEERSTYLE
  
  # @@protoc_insertion_point(class_scope:BeerStyle)

class BeerType(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BEERTYPE
  
  # @@protoc_insertion_point(class_scope:BeerType)

class Brewer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _BREWER
  
  # @@protoc_insertion_point(class_scope:Brewer)

class Drink(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DRINK
  
  # @@protoc_insertion_point(class_scope:Drink)

class Keg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEG
  
  # @@protoc_insertion_point(class_scope:Keg)

class KegSize(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEGSIZE
  
  # @@protoc_insertion_point(class_scope:KegSize)

class KegTap(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEGTAP
  
  # @@protoc_insertion_point(class_scope:KegTap)

class User(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USER
  
  # @@protoc_insertion_point(class_scope:User)

# @@protoc_insertion_point(module_scope)