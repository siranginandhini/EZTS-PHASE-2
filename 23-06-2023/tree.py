#dictionary (forest of three trees)
families={
           'charley':
                  {'sam':{'boxy','rosy'},
                   'niha':{'pepsi'}},
           'devi':
                  {'tommy':{'tony'},
                   'timmy':{'hamster'},
                   'tammy':{'hamster'}},
           'carlos':
                  {'diego':'cat','ferret':'fox'}
           }
for parent,childern in families.items():
    print(f"{parent} has {len(childern)} kids(s):")
    print(f"{', and '.join([str(child) for child in[*childern]])}")
