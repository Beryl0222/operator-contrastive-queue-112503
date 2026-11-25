"""验证业务输入之间的引用关系及形状，不计算目标输出。"""
import numpy as np
from support.inspect_data import load_bundle

def test_linked_materials():
    _, arrays, r, scenarios = load_bundle()
    for name in ('queries','positives','queue'):
        assert np.allclose(np.linalg.norm(arrays[name],axis=1),1)
    assert len(r['queries']) == arrays['queries'].shape[0]
    assert len(r['queue']) == arrays['queue'].shape[0]
    assert all(v['entity_id'] in r['current_labels'] for v in r['queue'])
