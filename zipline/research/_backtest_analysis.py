"""回测分析模块"""
import os
import errno
import pandas as pd
import pyfolio as pf


def create_full_tear_sheet(self):
    returns, positions, transactions = pf.utils.extract_rets_pos_txn_from_zipline(
        self)
    live_start_date = self.index[-int(len(self) / 4)]
    pf.create_full_tear_sheet(
        returns,
        positions=positions,
        transactions=transactions,
        live_start_date=live_start_date,
        round_trips=True)


def get_backtest(dir_name='~/.backtest'):
    """获取最近的回测结果(数据框)"""
    pref_root = os.path.expanduser(dir_name)
    try:
        candidates = os.listdir(pref_root)
        pref_file = os.path.join(pref_root, max(candidates))
        return pd.read_pickle(pref_file)
    except (ValueError, OSError) as e:
        if getattr(e, 'errno', errno.ENOENT) != errno.ENOENT:
            raise
        raise ValueError('在目录{}下，没有发现回测结果'.format(dir_name))


pd.DataFrame.create_full_tear_sheet = create_full_tear_sheet
