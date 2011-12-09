import flatland as fl


Enum_abc = fl.Enum.valued('A', 'B', 'C').with_properties(widget='radio')


Species = fl.Dict.of(
    fl.Integer.named('code'),
    fl.String.named('name'),
    fl.Dict.of(
            fl.String.named('resident'),
            fl.Dict.of(
                    fl.String.named('repro'),
                    fl.String.named('winter'),
                    fl.String.named('transit'),
                ).named('migratory').with_properties(
                    widget='dict',
                    order=['repro', 'winter', 'transit'],
                ),
        ).named('population').with_properties(
            widget='dict',
            order=['resident', 'migratory']),
    fl.Dict.of(
            Enum_abc.named('population'),
            Enum_abc.named('conservation'),
            Enum_abc.named('isolation'),
            Enum_abc.named('global'),
        ).named('site').with_properties(
            widget='dict',
            order=['population', 'conservation', 'isolation', 'global']),
).with_properties(order=['code', 'name', 'population', 'site'])
