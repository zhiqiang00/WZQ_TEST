from dragonfly.common_leaf_dsl import LeafService, LeafFlow

flow = LeafFlow(name="test") \
    .fake_retrieve(num=5, reason=999) \
    .gen_random_item_attr(
      attr_name = "random_int_attr",
      attr_type = "int"
    ) \
    .pack_item_attr(
      item_source = {
        "reco_results": True,
      },
      mappings = [{
        "from_item_attr": "random_int_attr",
        "to_common_attr": "random_common_attr",
      }]
    )

service = LeafService(kess_name="grpc_CommonLeafTest")
service.add_leaf_flows(leaf_flows=[flow])
leaf = service.executor()
leaf.run("test")