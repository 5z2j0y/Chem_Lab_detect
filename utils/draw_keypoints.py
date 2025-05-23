import cv2
import numpy as np
import torch


def draw_keypoints(image, keypoints, keypoint_conf=None, classes=None, box_conf=None):
    """
    绘制关键点到图像上
    
    参数:
        image: 原始图像
        keypoints: 关键点坐标 [num_objects, num_kpts, 2]
        keypoint_conf: 关键点置信度 [num_objects, num_kpts]
        classes: 检测框的类别 [num_objects]
        box_conf: 检测框置信度 [num_objects]
    
    返回:
        带有关键点的图像
    """
    img = image.copy()
    
    # 如果是PyTorch张量，转换为NumPy数组
    if isinstance(keypoints, torch.Tensor):
        keypoints = keypoints.cpu().numpy()
    if isinstance(keypoint_conf, torch.Tensor) and keypoint_conf is not None:
        keypoint_conf = keypoint_conf.cpu().numpy()
    if isinstance(classes, torch.Tensor) and classes is not None:
        classes = classes.cpu().numpy()
    if isinstance(box_conf, torch.Tensor) and box_conf is not None:
        box_conf = box_conf.cpu().numpy()

    # 为不同的类别预设不同的颜色
    colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0), (0, 255, 255)]
    
    # 绘制每个对象的关键点
    for i, kpts in enumerate(keypoints):
        # 选择颜色
        color_idx = int(classes[i]) if classes is not None else 0
        color = colors[color_idx % len(colors)]
        
        # 绘制关键点
        for j, (x, y) in enumerate(kpts):
            # 修改这里的条件判断逻辑，避免None与float比较
            conf_check = False
            if keypoint_conf is None:
                conf_check = True
            elif j < len(keypoint_conf[i]) and keypoint_conf[i][j] is not None and keypoint_conf[i][j] > 0.5:
                conf_check = True
                
            if conf_check:
                cv2.circle(img, (int(x), int(y)), 5, color, -1)
        
        # 如果有类别和置信度信息，添加标签
        if classes is not None and box_conf is not None:
            label = f"Class: {int(classes[i])}, Conf: {box_conf[i]:.2f}"
            cv2.putText(img, label, (int(kpts[0][0]), int(kpts[0][1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    return img
