import tensorflow as tf
import numpy as np

# ��Ӳ�
def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

# 1.ѵ��������
# Make up some real data 
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# 2.����ڵ�׼����������
# define placeholder for inputs to network  
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

# 3.�����񾭲㣺���ز��Ԥ���
# add hidden layer ����ֵ�� xs�������ز��� 10 ����Ԫ   
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# add output layer ����ֵ�����ز� l1����Ԥ������ 1 �����
prediction = add_layer(l1, 10, 1, activation_function=None)

# 4.���� loss ���ʽ
# the error between prediciton and real data    
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                     reduction_indices=[1]))

# 5.ѡ�� optimizer ʹ loss �ﵽ��С                   
# ��һ�ж�������ʲô��ʽȥ���� loss��ѧϰ���� 0.1       
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


# important step �����б������г�ʼ��
init = tf.initialize_all_variables()
sess = tf.Session()
# ���涨��Ķ�û�����㣬ֱ�� sess.run �ŻῪʼ����
sess.run(init)

# ���� 1000 ��ѧϰ��sess.run optimizer
for i in range(1000):
    # training train_step �� loss ������ placeholder ��������㣬��������Ҫ�� feed �������
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to see the step improvement
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))

