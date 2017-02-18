init offset = -100

init python:

    class Attribute(renpy.object.Object):
        """
        Represents a mapping from an attribute to an image as part of an
        attribute image. An attribute can be mapped to multiple images, in
        which case all images corresponding to that attribute will be
        displayed.

        `group`
            A string giving the group the attribute is part of. An attribute
            must belong to a single group, and the attribute conflicts with
            other attributes in that group.

        `attribute`
            A string giving the name of the attribute.

        `offset`
            If not None, a tuple giving the offset of the attribute from
            the top left of the image.

        `image`
            If not None, this should be a displayable that is displayed when
            this attribute is shown.

        Other keyword arguments are interpreted as transform properties. If
        any are present, a transform is created that wraps the image. (For
        example, pos=(100, 200) can be used to offset the image by 100 pixels
        horizontally and 200 vertically.)

        If the `image` parameter is omitted or None, and the AttributeImage
        has been given the `image_format` parameter, the image_format is used
        to generate an image filename.
        """


        def __init__(self, group, attribute,  image=None, default=False, **kwargs):

            self.group = group
            self.attribute = attribute
            self.image = image
            self.default = default

            self.transform_args = kwargs

        def apply_format(self, format):

            if self.image is None:

                if format is None:
                    raise Exception("Attribute(%r, %r) was not given an image parameter.".format(self.group, self.attribute))

                self.image = format.format(group=self.group, attribute=self.attribute)

            elif isinstance(self.image, basestring):

                self.image = format.format(group=self.group, attribute=self.attribute, image=self.image)


            if self.transform_args:

                self.image = Transform(self.image, **self.transform_args)


    class AttributeImage(renpy.object.Object):
        """
        This is an image-like object that, when shown with the proper set of
        attributes, shows a displayable created by compositing together the
        displayables associated with those attribute.

        `attributes`
            This must be a list of Attribute objects. Each Attribute object
            reflects a displayable that may or may not be displayed as part
            of the image. The items in this list are in back-to-front order,
            with the first item further from the viewer and the last
            closest.

        `image_format`
            If not None, this should be a string giving a Python format pattern.
            If an attribute is not given the image parameter, "{group}" is replaced
            with the involved group, "{attribute}" is replaced with the involved
            attribute, and the image so produced is used instead. If the attribute
            is given a string as an image paramter, "{image}" is replaced with
            by that parameter, in addition to the "{group}" and "{attribute}"
            substitutions.

        """

        def __init__(self, attributes, image_format=None):

            self.image_format = image_format

            self.attributes = [ ]

            import collections
            self.attribute_to_groups = collections.defaultdict(set)
            self.group_to_attributes = collections.defaultdict(set)

            for i in attributes:
                self.add(i)

                if i.group is not None:
                    self.attribute_to_groups[i.attribute].add(i.group)
                    self.group_to_attributes[i.group].add(i.attribute)

        def add(self, a):
            a.apply_format(self.image_format)
            self.attributes.append(a)

        def get_banned(self, attributes):
            """
            Get the set of attributes that are incompatible with those
            in attributes.
            """

            rv = set()

            for i in attributes:
                for g in self.attribute_to_groups[i]:
                    for j in self.group_to_attributes[g]:
                        if j != i:
                            rv.add(j)
            return rv

        def _duplicate(self, args):

            name = " ".join(args.name + tuple(args.args))

            attributes = set(args.args)
            banned = self.get_banned(attributes)

            for a in self.attributes:
                if a.default and (a.attribute not in banned):
                    attributes.add(a.attribute)

            rv = Fixed(xfit=True, yfit=True)

            for a in self.attributes:
                if a.attribute in attributes:
                    rv.add(a.image)

            return rv

        def _list_attributes(self, attributes):
            banned = self.get_banned(attributes)

            rv = [ ]
            seen = set()

            for a in self.attributes:
                if a.attribute in banned:
                    continue

                if a.attribute in seen:
                    continue

                seen.add(a.attribute)
                rv.add(a.attribute)

            return rv

        def _choose_attributes(self, tag, attributes, optional):

            attributes = set(attributes)
            banned = self.get_banned(attributes)

            both = attributes & banned

            if both:
                raise Exception("The attributes for {} conflict: {}".format(tag, " ".join(both)))


            if optional is not None:
                attributes |= (set(optional) - banned)

            rv = [ ]

            for a in self.attributes:
                if a.attribute in attributes:
                    rv.append(a.attribute)
                    attributes.remove(a.attribute)

            return tuple(rv)






