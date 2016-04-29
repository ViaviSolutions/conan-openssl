from conan.packager import ConanMultiPackager


def efence_options(options, no_electric_fence):
    new_option_items = [
        ('OpenSSL:no_electric_fence', True),
        ('OpenSSL:zlib_dynamic', options['OpenSSL:shared'])
        ]
    return dict(options.items() + new_option_items)


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds(shared_option_name="OpenSSL:shared", pure_c=True)
    efence_builds = []
    for settings, options in builder.builds:
        efence_builds.append([settings, efence_options(options, True)])
        efence_builds.append([settings, efence_options(options, False)])
    builder.builds = efence_builds
    builder.run()
