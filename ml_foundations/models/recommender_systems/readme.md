- how to predict the rating a user might give to a prospective item
- how to generate a recommendation list of items0
- how to predict the click-through rate from abundant features.

Overview of Recommender Systems
- Collaborative Filtering: 
  the data is user-item data.
  - memory based (nearest neighbors based CF: user based or item based). It has limitation of dealing with sparse and large dataset.
  - model based (latent factor models: matrix factorization). It deals with sparse and large dataset effectively. Many of these even can be extended with NN. 
  - and their hybrid
- Content based systems: contents descriptions of items/users
- Context based systems: context like timestamps and locations
- Explicit Feedback and Implicit Feedback:
  explicit: youtube likes, imdb ratings. It is hard to collect as user needs to proactive to give the feedbacks.
  implicit: user clicks, purchase history, browsing history, watches and even mouse movements. The implicit data is very noisy.
 
 