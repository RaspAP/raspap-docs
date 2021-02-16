![](https://i.imgur.com/eEXpMlO.png)

RaspAP is rolling out a [sponsorware release model](https://github.com/sponsors/RaspAP), which means that new features are first exclusively released to sponsors as part of **Insiders**. Read on to learn how sponsorship works, and how easy it is to get access to Insiders.

## How sponsorship works
New features first land in [**Insiders**](https://github.com/sponsors/RaspAP), which means that *sponsors will have access to them immediately*. Every feature is tied to a funding goal in monthly subscriptions. When a funding goal is hit, the features that are tied to it are merged back into the [public RaspAP repository](https://github.com/RaspAP/raspap-webgui) and released for general availability.
Bug fixes, translation updates and minor enhancements are always released simultaneously in both editions.[^1]

*Don't want to sponsor? No problem, RaspAP already has tons of features available, so chances are that most of your requirements are already satisfied. See the list of [exclusive features](#exclusive-features) to learn which features are currently only available to sponsors.*

## How to become a sponsor
You can become a sponsor using your individual or organization's GitHub account. Just [pick any tier from $10/month](https://github.com/sponsors/RaspAP) and complete the checkout.
Then, after a few hours, you will be added as a team member to the super-secret private GitHub repository containing the Insiders edition, which has all exclusive features.
In addition, you get access to Insiders-only team discussions and content.

> :information_source: **Important**: If you're sponsoring [RaspAP](https://github.com/RaspAP/sponsors) through a GitHub organization, please send a short email to [sponsors@raspap.com](mailto:sponsors@raspap.com) with the name of your organization and the account that should be added as a collaborator.[^2] 

You can cancel your sponsorship anytime.[^3]

## Exclusive features
When backers were asked which feature they'd most like to see added to RaspAP, the ability to manage multiple OpenVPN client configurations topped the list of requests.
We think this is a great idea, so we've added this as the first feature exclusive to Insiders. 

:octicons-check-circle-fill-24:{: .check } [Multiple OpenVPN client configs](/openvpn/#multiple-client-configs)    
:octicons-check-circle-fill-24:{: .check } OpenVPN service logging  
:octicons-check-circle-fill-24:{: .check } Night mode toggle  
:gear: Traffic shaping (in progress)  

Look for the list above to grow as we add more exclusive features. 

## Funding targets
Below is a list of funding targets. When a funding target is reached, the features that are tied to it are merged back into RaspAP and released to the public for general availability.

### Goals
#### **$500** - First Insiders Edition
:octicons-check-circle-fill-24:{: .check } [Multiple OpenVPN client configs](/openvpn/#multiple-client-configs)  
:octicons-check-circle-fill-24:{: .check } OpenVPN service logging  
:octicons-check-circle-fill-24:{: .check } Night mode toggle  
:gear: Traffic shaping (in progress)  

## Transparency
We've chosen [OpenCollective](https://opencollective.com/raspap) as the fiscal host for our [GitHub sponsors organization](https://github.com/sponsors/RaspAP). This means that our budget is completely transparent—
financial contributions, expenses and payouts to project team members are automatically reported. Everyone can see where money comes from and what it's spent on. This committent to full transparency
was central in our decision to implement Insiders.

## Frequently asked questions

### Upgrading
*I have an existing RaspAP installation. How do I upgrade to Insiders?*

Upgrading is easy. Simply invoke the [Quick Installer](https://docs.raspap.com/quick/) with the `--upgrade` switch, specifying the private Insiders repo, like so:

```
curl -sL https://install.raspap.com | bash -s -- --upgrade --repo raspap/raspap-insiders
```

If you haven't [added SSH keys to your GitHub account](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) you will be prompted to authenticate.
In this case, just enter your GitHub credentials during the install. For example:

```
RaspAP Install: Cloning latest files from github
Cloning into '/tmp/raspap-webgui'...
Username for 'https://github.com': octocat
Password for 'https://octocat@github.com': 
```

> :information_source: **Note**: your password is sent securely via SSH to GitHub. The above prompt is actually from GitHub, so the installer does _not_ know your credentials.

### Terms
*We're using RaspAP for a commercial project. Can we use Insiders under the same terms and conditions?*

Yes. Whether you're an individual or a company, you may use RaspAP Insiders precisely under the same terms as RaspAP, which are defined by the [GNU GPL 3.0 license](https://github.com/RaspAP/raspap-webgui/blob/master/LICENSE). However, we kindly ask you to respect the following guidelines:

* Please **don't distribute the source code** of Insiders. You may freely use it for public, private or commercial projects, fork it, mirror it, do whatever you want with it, but please don't release the source code, as it would counteract the sponsorware strategy.
* If you cancel your subscription, you're removed as a collaborator and will miss out on future updates of Insiders. However, you may *use the latest version* that's available to you as long as you like. Just remember that [GitHub deletes private forks](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/removing-a-collaborator-from-a-personal-repository).

[^1]: You may be wondering if the sponsorware model contradicts the ethos of Open Source software. It's true that some features are locked behind a payment, which means they are only accessible after pledging a small amount of money.
However, these features are only exclusive until specific funding targets are reached. Making an Open Source project sustainable is exceptionally difficult. Maintainers invest significant time and energy
developing software, testing, responding to issues, writing documentation and so on. Too often, this leads to burnout and abandoned projects.
The sponsorware model ensures that if you decide to use RaspAP, you can be sure that the project remains healthy, bugs are fixed quickly and new features are added regularly. 

[^2]: It's currently not possible to grant access to each member of an organization, as GitHub only allows for adding users. Thus, after sponsoring, please send an email to [sponsors@raspap.com](mailto:sponsors@raspap.com),
stating which account should become a collaborator of the Insiders repository. We're working on a solution which will make access to organizations much simpler.

[^3]: If you cancel your sponsorship, GitHub schedules a cancellation request which will become effective at the end of the billing cycle, which ends at the 22^nd^ of the month for monthly sponsorships.
This means that even though you cancel your sponsorship, you will keep your access to Insiders as long as your cancellation isn't effective. All charges are processed by GitHub through Stripe.
As we don't receive any information regarding your payment, and GitHub doesn't offer refunds, sponsorships are non-refundable.


