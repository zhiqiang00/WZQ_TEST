from dragonfly.common_leaf_dsl import LeafService, LeafFlow
import os
flow = LeafFlow(name="test")
current_folder = os.path.dirname(os.path.abspath(__file__))

flow.fake_retrieve(num=5, reason=999) \
  .enrich_attr_by_lua(
    function_for_item = "calculate",
    export_item_attr = ["item_text"],
    lua_script = """
      function calculate(seq, item_key, reason, score)
        local item_text = 'Hello ItemAttr'
        return item_text
      end
    """
  ) \
  .gen_common_attr_by_lua(
    attr_map={
      "common_text": "'Hello CommonAttr'"
    }
  ) \
  .log_debug_info(
    for_debug_request_only = False,
    common_attrs = [
      "common_text",
    ],
    item_attrs = [
      "item_text",
    ]
  )

service = LeafService(kess_name="grpc_CommonLeafTest")
service.add_leaf_flows(leaf_flows=[flow], request_type="default") \
       .draw(dag_folder=current_folder) \
       .build(output_file=os.path.join(current_folder, "dragonfly_demo.json"))