import chainer
import onnx

from onnx_chainer.functions.opset_version import support


@support((1, 6, 7))
def convert_Dropout(
        func, opset_version, input_names,
        output_names, context, parameters):
    if opset_version == 1:
        return onnx.helper.make_node(
            'Dropout', input_names, output_names,
            is_test=0 if chainer.config.train else 1,
            ratio=func.dropout_ratio,
            consumed_inputs=[1]
        ),
    elif opset_version == 6:
        return onnx.helper.make_node(
            'Dropout', input_names, output_names,
            is_test=0 if chainer.config.train else 1,
            ratio=func.dropout_ratio,
        ),
    elif opset_version == 7:
        return onnx.helper.make_node(
            'Dropout', input_names, output_names,
            ratio=func.dropout_ratio,
        ),
