import pandas as pd

from enum import Enum


class JoinMode(Enum):
    inner_join = 0
    left_outer_join = 1
    right_outer_join = 2
    full_outer_join = 3


def merge_join(
    left: pd.DataFrame,
    right: pd.DataFrame,
    attributes: list[str],
    mode: JoinMode = JoinMode.inner_join,
) -> pd.DataFrame:
    left = left.sort_values(by=attributes)
    right = right.sort_values(by=attributes)
    left_merged = left[attributes]
    right_merged = right[attributes]
    left_i, right_i = 0, 0
    left_indices = []
    right_indices = []

    while left_i < left.shape[0] or right_i < right.shape[0]:
        if left_i == left.shape[0]:
            if mode == JoinMode.right_outer_join or mode == JoinMode.full_outer_join:
                right_indices.append(right_i)
            right_i += 1
        elif right_i == right.shape[0]:
            if mode == JoinMode.left_outer_join or mode == JoinMode.full_outer_join:
                left_indices.append(left_i)
            left_i += 1
        elif left_merged.iloc[left_i].values == right_merged.iloc[right_i].values:
            left_indices.append(left_i)
            right_indices.append(right_i)
            left_i += 1
            right_i += 1
        elif left_merged.iloc[left_i].values < right_merged.iloc[right_i].values:
            if mode == JoinMode.left_outer_join or mode == JoinMode.full_outer_join:
                left_indices.append(left_i)
            left_i += 1
        else:
            if mode == JoinMode.right_outer_join or mode == JoinMode.full_outer_join:
                right_indices.append(right_i)
            right_i += 1
    if mode == JoinMode.left_outer_join or mode == JoinMode.inner_join:
        left = left.iloc[left_indices]
        right = right.iloc[right_indices].drop(columns=attributes)
        for column in right:
            left[column] = right[column]
        return left
    elif mode == JoinMode.right_outer_join:
        left = left.iloc[left_indices]
        right = right.iloc[right_indices].drop(columns=attributes)
        for column in left:
            right[column] = left[column]
        return right
    else:
        left = left.iloc[left_indices]
        right = right.iloc[right_indices].drop(columns=attributes)
        out = pd.concat(objs=[left, right], axis=1)
        return out
