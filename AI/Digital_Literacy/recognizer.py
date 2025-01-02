import numpy as np
import joblib

default_values = [
    0.2907713055610657, 0.9902615547180176, 8.740216799196787e-07, 0.44163498282432556,
    0.8783921003341675, 0.02843230590224266, 0.5060588717460632, 0.755861759185791,
    0.047979533672332764, 0.5527979135513306, 0.6539841890335083, 0.04704081267118454,
    0.5684658885002136, 0.559204638004303, 0.0485905259847641, 0.3517342209815979,
    0.6541176438331604, 0.13134944438934326, 0.3703639507293701, 0.5233951210975647,
    0.11456790566444397, 0.45519372820854187, 0.515338122844696, 0.08193530142307281,
    0.5219626426696777, 0.541510820388794, 0.06341321766376495, 0.31640034914016724,
    0.6418271660804749, 0.09433136135339737, 0.3417103886604309, 0.48047584295272827,
    0.0682794377207756, 0.4474653899669647, 0.48046422004699707, 0.019834019243717194,
    0.5184870362281799, 0.5373350381851196, -0.008702876046299934, 0.2878860831260681,
    0.6325947046279907, 0.04804195463657379, 0.32118478417396545, 0.46004337072372437,
    0.024638723582029343, 0.42739349603652954, 0.464252233505249, -0.012213464826345444,
    0.49689099192619324, 0.5220650434494019, -0.03060729056596756, 0.26204341650009155,
    0.6315548419952393, 0.0012936360435560346, 0.30556046962738037, 0.4906770586967468,
    -0.010521531105041504, 0.39576709270477295, 0.4696756899356842, -0.02468831278383732,
    0.4667765200138092, 0.49477919936180115, -0.032252196222543716
]

default_values = np.array(default_values).reshape(1, -1)

predicted_label = rf_classifier.predict(default_values)

print("Predicted Label:", predicted_label[0])